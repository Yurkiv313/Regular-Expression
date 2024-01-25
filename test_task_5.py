from task_5 import split_text_into_sentences


def test_split_text_into_sentences():
    text = "Мене звати Андрій. Я пишу цей текст."
    sentences = split_text_into_sentences(text)
    print(sentences)
    assert sentences == ["Мене звати Андрій.", "Я пишу цей текст."]


test_split_text_into_sentences()
