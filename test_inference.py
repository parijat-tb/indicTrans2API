from inference import IndicTrans2Translator

def test_translation():
    # Test English to Hindi
    print("Testing English to Hindi...")
    en_indic_model = "ai4bharat/indictrans2-en-indic-1B"
    translator = IndicTrans2Translator(model_name=en_indic_model)
    
    sentences = [
        "Hello, how are you?",
        "This is a test sentence."
    ]
    src_lang = "eng_Latn"
    tgt_lang = "hin_Deva"
    
    translations = translator.translate(sentences, src_lang, tgt_lang)
    for src, tgt in zip(sentences, translations):
        print(f"{src} -> {tgt}")
        
    print("\nTranslation test complete.")

if __name__ == "__main__":
    test_translation()
