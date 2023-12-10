from transformers import AutoModelForSeq2SeqLM, T5TokenizerFast

MODEL_NAME = 'UrukHan/t5-russian-summarization'
MAX_INPUT = 256000000


def summary(text: str, sentence_count: int) -> list[str]:
    tokenizer = T5TokenizerFast.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

    input_sequences = text
    if type(input_sequences) != list:
        input_sequences = [input_sequences]

    task_prefix = ""
    inp = ''.join(input_sequences).split('.')

    combined_arr = []
    for i in range(0, len(inp), sentence_count):
        combined_string = ". ".join(inp[i:i + sentence_count])
        combined_arr.append(combined_string.strip())

    combined_arr = [s for s in combined_arr if len(s) > 10]

    encoded = tokenizer(
        [task_prefix + sequence for sequence in combined_arr],
        padding="longest",
        truncation=True,
        return_tensors="pt",
    )
    predicts = model.generate(**encoded)
    result = tokenizer.batch_decode(predicts, skip_special_tokens=True)

    return result
