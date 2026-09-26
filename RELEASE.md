# Release notes

## 1.0 (2026-09-26)

This release fixes the search page, adds carrier density to quantized Hall resistance (QHR) measurements, and documents how to set up and run pyMDSS. It includes one database migration.

### New

- **Carrier density for QHR measurements.** `QHR_Process` has a new `carrier_density` field, stored in the column `Carrier density` right after `Characterization cryostat`. It is optional: rows uploaded before this release have no value (NULL).
- **QHR uploads accept both file formats.**
  - Old format (49 values per line): carrier density is left empty.
  - New format (50 values per line): carrier density comes right after the characterization cryostat value. A blank value is stored as empty.
- **README.md** with installation, database setup, launch and troubleshooting instructions.
- **.gitignore** for secrets (`.env`, certificates), database dumps, logs and compiled Python files.

### Fixed

- **Search crashed when a download format was entered.** Typing `xlsx` or `text` in the Format box caused a server error. Format now only selects the file type. This affected both standard resistor and quantized conductance search.
- **Searching on more than one field returned no results or the wrong ones.** Values were matched to the wrong columns; for example, the serial number was looked up in the Nominal column. Each value is now matched to its own column.
- **QHR lines with the wrong number of values were skipped silently.** The file was still reported as uploaded, so it could not be uploaded again. Such a file is now rejected with an error and can be re-uploaded once fixed.
- **One failed file in a multi-file QHR upload marked all later files as failed.** Their rows were saved but their file names were not recorded, so uploading them again duplicated data.

### Changed

- Compiled Python files (`__pycache__/*.pyc`) are no longer tracked in git.
- `help.md` includes the `CREATE USER` step.
- The page footer shows version 1.0.

### Upgrading from 0.3

No new Python packages are needed, and static files are unchanged.

1. Stop the Celery worker and the web server, and back up the `mdss` database.
2. Pull the new code. If `git pull` refuses because `.pyc` files were modified, run `git checkout -- "*.pyc"` first. If `pymdss/pymdss/.env` is missing afterwards, restore it from a backup.
3. From `pymdss/`, run `python manage.py migrate`. It applies `qconductance.0006_qhr_process_carrier_density`.
4. Start the Celery worker and the web server. The worker must start after the migration.
5. Switch the measurement software to the new QHR file format when ready. Old-format files are still accepted.

To roll back, run `python manage.py migrate qconductance 0005` **before** checking out the 0.3 code. This removes the `Carrier density` column and any values in it.

### Tested with

Windows 11, Python 3.12.4, Django 5.2.17, MySQL 8.0.46, Redis 3.0.504 (Windows port) with redis-py 5.3.1, and Celery 5.6.3, using a copy of the production database restored from the 2026-09-25 backup.

- The main pages load over HTTPS, search and Excel export work, and uploads are processed by the Celery worker.
- Migration 0006 was applied to the restored data, and to a fresh test database where it was also rolled back. Seven temporary automated tests covered the column position, old, new and blank-value QHR files, rejected files, multi-file uploads and the rollback. These tests are not yet part of the repository.

Django 6 needs MySQL 8.4 or later, so use Django 5.2 LTS with MySQL 8.0. The Windows port of Redis (3.0) needs redis-py below 6.

### Known issues

- `/redirect` returns a server error: the URL points at Django's `redirect()` helper instead of a view.
- `/capacitorIndex/` renders a template that doesn't exist (`capacitorIndex.html`; the file is named `capacitors-index.html`).
- `check_task_status/<task id>/` returns a server error for tasks that are still running or have failed. The upload progress bar uses a different endpoint and is not affected.
- Standard resistor uploads still have the multi-file problem that this release fixes for QHR uploads.
- A search on one field is exact and case-sensitive; a search on several fields ignores case.
- On Django 5.1 and later the `STATICFILES_STORAGE` setting is ignored, so static files lose their versioned names and browsers can keep old CSS and JavaScript cached for up to a year after it changes. Replace it with the `STORAGES` setting.
- `Dockerfile` and `docker-compose.yml` are out of date and don't build.

### AI assistance

The code changes, tests and documentation in this release were developed with AI assistance: Claude (Anthropic's Claude Opus 5.5 model) in Claude Code, working under the maintainer's direction, with the maintainer approving each change before it was committed. Commits made with AI assistance carry a `Co-Authored-By: Claude` trailer.

Commits in this release: [84e9583](https://github.com/usnistgov/pyMDSS/commit/84e9583), [2e38147](https://github.com/usnistgov/pyMDSS/commit/2e38147), [68603ca](https://github.com/usnistgov/pyMDSS/commit/68603ca), [35fbc2f](https://github.com/usnistgov/pyMDSS/commit/35fbc2f), plus the version 1.0 update.
