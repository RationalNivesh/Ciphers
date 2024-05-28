message =input("What is your message")
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop over every possible key
for key in range(len(SYMBOLS)):
    translated = ''
    # Loop over each symbol in the message
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            
            # Handle wrap-around if translatedIndex is less than 0
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            
            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Just add the symbol without encrypting/decrypting if it's not in SYMBOLS
            translated = translated + symbol
    
    print('Key #%s: %s' % (key, translated))
