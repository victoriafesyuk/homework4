
import json
from wer import calculate_wer


def read_text(file_path):
    """Читає текст із файлу."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def save_metrics(reference_path, hypothesis_path, output_path):
    """Обчислює WER і зберігає метрики у JSON."""

    reference = read_text(reference_path)
    hypothesis = read_text(hypothesis_path)

    result = calculate_wer(reference, hypothesis)

    metrics = {
        "WER": result["wer"],
        "S": result["substitutions"],
        "D": result["deletions"],
        "I": result["insertions"],
        "N": result["reference_words"]
    }

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(metrics, file, ensure_ascii=False, indent=4)

    print("Метрики збережено у файл", output_path)
    print(json.dumps(metrics, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    save_metrics(
        "reference.txt",
        "hypothesis.txt",
        "results.json"
    )
