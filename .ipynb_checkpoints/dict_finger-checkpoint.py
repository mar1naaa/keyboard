"""keylout_dd = {rfi5:[(кортеж_мизинца_правой_для_ЙЦУКЕН), (кортеж_мизинца_правой_для_ДРУГОЙ)],  rfi4:[(… ...),...],...
rfi3:[...], rfi2:[...], lfi5:[…], lfi4:[…].… }"""

keyboard_finger_qwerty = {
    lfi5 : ('ё','1','й','ф','я'),
    lfi4 : ('2','ц','ы','ч'),
    lfi3 : ('3','у','в','с'),
    lfi2 : ('4','к','а','м','5','е','п','и'),
    lfi1 : (' '),
    rfi2 : ('6','н','р','т','7','г','о','ь'),
    rfi3 : ('8','ш','л','б'),
    rfi4 : ('9','щ','д','ю'),
    rfi5 : ('0','-','=','з','ж','.','х','э','ъ')
    
}
keyboard_finger_vyzov = {
    lfi5 : ('ю','ё','в','ч','ш'),
    lfi4 : ('ы','и','х','['),
    lfi3 : ('э','о','е','й'),
    lfi2 : ('Э','у','а','к','(','ь',',','_'),
    lfi1 : (' '),
    rfi2 : ('=','*','ё','.','/','^','н','р'),
    rfi3 : (')','д','т','м'),
    rfi4 : ('+','я','с','ф'),
    rfi5 : (']','!','щ','г','ж','ц','б','з','п','ъ')
    
}


vyzov_finger_count = {'lfi5': 0, 'lfi4': 0, 'lfi3': 0, 'lfi2': 0, 'lfi1': 0, 'rfi2': 0, 'rfi3': 0, 'rfi4': 0, 'rfi5': 0}
qwerty_finger_count = {'lfi5': 0, 'lfi4': 0, 'lfi3': 0, 'lfi2': 0, 'lfi1': 0, 'rfi2': 0, 'rfi3': 0, 'rfi4': 0, 'rfi5': 0}