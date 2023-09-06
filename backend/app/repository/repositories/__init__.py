from .cv_repo import get_cv_repository as cv_repo
from .vacancy_repo import get_vacancy_repository as vacancy_repo
from .cv_note_repo import get_cv_note_repository as cv_note_repo
from .vacancy_note_repo import get_vacancy_note_repository as vacancy_note_repo
from .user_repo import get_user_repository as user_repo


__all__ = (
    "cv_repo",
    "vacancy_repo",
    "cv_note_repo",
    "vacancy_note_repo",
    "user_repo",
)