from deep_translator import GoogleTranslator

def translate_text():
    print("\n----- Language Translation System -----")

    text = input("Enter English text: ")

    print("\nChoose language:")
    print("1. Hindi")
    print("2. Marathi")
    print("3. French")
    print("4. Spanish")

    choice = input("Enter choice (1-4): ")

    lang_map = {
        "1": "hi",
        "2": "mr",
        "3": "fr",
        "4": "es"
    }

    try:
        translated = GoogleTranslator(source='auto', target=lang_map[choice]).translate(text)

        print("\nOriginal Text:", text)
        print("Translated Text:", translated)

    except Exception as e:
        print("Error:", e)

while True:
    translate_text()
    if input("\nContinue? (yes/no): ").lower() != "yes":
        break