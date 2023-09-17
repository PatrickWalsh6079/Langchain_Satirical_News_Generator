import spacy
from langchain_experimental.data_anonymizer import PresidioReversibleAnonymizer

spacy.load('en_core_web_lg')


def anonymize(text):
    anonymizer = PresidioReversibleAnonymizer(
        analyzed_fields=["PERSON", "ORGANIZATION", "LOCATION", "PHONE_NUMBER", "EMAIL_ADDRESS", "US_SSN"]
    )
    return anonymizer.anonymize(text)
