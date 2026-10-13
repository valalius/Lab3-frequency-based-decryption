# Еталонні частоти літер
ENGLISH_FREQS = {
    'A': 8.08,  'B': 1.67,  'C': 3.18,  'D': 3.99,  'E': 12.56,
    'F': 2.17,  'G': 1.80,  'H': 5.27,  'I': 7.24,  'J': 0.14,
    'K': 0.63,  'L': 4.04,  'M': 2.60,  'N': 7.38,  'O': 7.47,
    'P': 1.91,  'Q': 0.09,  'R': 6.42,  'S': 6.59,  'T': 9.15,
    'U': 2.79,  'V': 1.00,  'W': 1.89,  'X': 0.21,  'Y': 1.65,
    'Z': 0.07
}

def decrypt_text(text: str, shift: int) -> str:
    # Розшифрування тексту за заданим зсувом shift зі збереженням регістра
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') - shift) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') - shift) % 26 + ord('A')))
        else:
            result.append(ch)
    return "".join(result)

def calculate_chi_squared(text: str) -> float:
    # Обчислення статистики хі-квадрата для тексту
    # Підрахунок літер (case-insensitive)
    counts = {chr(ord('A') + i): 0 for i in range(26)}
    total_letters = 0
    for ch in text:
        upper_ch = ch.upper()
        if 'A' <= upper_ch <= 'Z':
            counts[upper_ch] += 1
            total_letters += 1

    if total_letters == 0:
        return float('inf')

    chi_sq = 0.0
    for letter, observed in counts.items():
        expected = total_letters * (ENGLISH_FREQS[letter] / 100.0)
        chi_sq += ((observed - expected) ** 2) / expected

    return chi_sq

def main():
    message = input()

    best_shift = 0
    min_chi_sq = float('inf')

    # Усі можливі зсуви від 0 до 25
    for shift in range(26):
        decrypted_candidate = decrypt_text(message, shift)
        score = calculate_chi_squared(decrypted_candidate)

        if score < min_chi_sq:
            min_chi_sq = score
            best_shift = shift

    # Фінальний розшифрований рядок
    print(decrypt_text(message, best_shift))

if __name__ == '__main__':
    main()