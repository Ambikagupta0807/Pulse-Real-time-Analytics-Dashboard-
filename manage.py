#!/usr/bin/env python
import os
import sys
import asyncio

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard_project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django..."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()