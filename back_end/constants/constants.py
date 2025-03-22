import os

##-----LLM Models-----##
# PORTFOLIO ASSISTANT MODEL
ASSISTANT_MODEL = "gemini-1.5-flash"
# SPEECH-TO-TEXT MODEL
SPEECH_TO_TEXT_MODEL = "whisper-1"

##-----FILE DIRECTORIES-----##
ROOTPATH = os.getcwd()
EDUCATION_BACKGROUND_DIRECTORY = os.path.join(ROOTPATH, "files\education_background")
EXPERIENCE_LETTERS_DIRECTORY = os.path.join(ROOTPATH, "files\experience_letters")
MY_IMAGES_DIRECTORY = os.path.join(ROOTPATH, "files\my_images")
OTHER_FILES_DIRECTORY = os.path.join(ROOTPATH, "files\other")
PERSONAL_DOCUMENTS_DIRECTORY = os.path.join(ROOTPATH, "files\personal_documents")
PROJECTS_DIRECTORY = os.path.join(ROOTPATH, "files\projects")
RESUME_DIRECTORY = os.path.join(ROOTPATH, "files\resume")
SALARY_SLIPS_DIRECTORY = os.path.join(ROOTPATH, "files\salary_slips")
