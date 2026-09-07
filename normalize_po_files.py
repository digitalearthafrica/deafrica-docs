"""Normalize Gettext PO files before compiling them."""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
import sys

import polib


LOCALE_DIR = Path("locales/fr/LC_MESSAGES")


def align_leading_newline(source: str, translation: str) -> tuple[str, bool]:
    """
    Make the translation agree with the source about a leading newline.

    Gettext requires msgid and msgstr to either both begin with a newline
    or both begin without one.
    """
    source_starts_newline = source.startswith("\n")
    translation_starts_newline = translation.startswith("\n")

    if source_starts_newline and not translation_starts_newline:
        return f"\n{translation}", True

    if not source_starts_newline and translation_starts_newline:
        return translation[1:], True

    return translation, False


def normalize_po_file(po_path: Path) -> int:
    """Normalize one PO file and return the number of changed entries."""
    catalogue = polib.pofile(str(po_path))
    changed_entries = 0

    # Complete the standard metadata fields reported by msgfmt.
    metadata_updates = {
        "PO-Revision-Date": datetime.now(UTC).strftime("%Y-%m-%d %H:%M%z"),
        "Last-Translator": "Digital Earth Africa Translation Workflow",
        "Language-Team": "French",
        "Language": "fr",
        "Content-Type": "text/plain; charset=UTF-8",
        "Content-Transfer-Encoding": "8bit",
        "Plural-Forms": "nplurals=2; plural=(n > 1);",
    }

    for key, value in metadata_updates.items():
        if not catalogue.metadata.get(key):
            catalogue.metadata[key] = value

    for entry in catalogue:
        if entry.obsolete:
            continue

        entry_changed = False

        if entry.msgid_plural:
            # Use the singular source for plural form 0 and plural source
            # for the remaining French plural forms.
            for plural_index, translation in entry.msgstr_plural.items():
                source = (
                    entry.msgid
                    if str(plural_index) == "0"
                    else entry.msgid_plural
                )

                normalized, changed = align_leading_newline(
                    source,
                    translation,
                )

                if changed:
                    entry.msgstr_plural[plural_index] = normalized
                    entry_changed = True
        else:
            normalized, changed = align_leading_newline(
                entry.msgid,
                entry.msgstr,
            )

            if changed:
                entry.msgstr = normalized
                entry_changed = True

        if entry_changed:
            changed_entries += 1

    catalogue.save(str(po_path))
    return changed_entries


def main() -> None:
    po_files = sorted(LOCALE_DIR.rglob("*.po"))

    if not po_files:
        raise FileNotFoundError(
            f"No PO files were found under {LOCALE_DIR}."
        )

    total_changes = 0

    for po_file in po_files:
        changed = normalize_po_file(po_file)
        total_changes += changed
        print(f"Normalized {po_file}: {changed} changed entries")

    print(
        f"Normalization complete: {total_changes} entries changed "
        f"across {len(po_files)} PO file(s)."
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"PO normalization failed: {error}", file=sys.stderr)
        raise