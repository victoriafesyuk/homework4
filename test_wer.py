
from wer import calculate_wer

reference = "The cat is on the mat"
hypothesis = "The kat is not on mat today"

result = calculate_wer(reference, hypothesis)

print("Word Error Rate:", result["wer"], "%")
print("Заміни:", result["substitutions"])
print("Пропуски:", result["deletions"])
print("Додавання:", result["insertions"])
print("Кількість слів в еталоні:", result["reference_words"])
