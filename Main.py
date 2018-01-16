from PyQt5 import QtWidgets, QtGui, QtCore, uic
import sys
import random as rd
import itertools as it

'''result = ''

with open('words.txt', encoding='utf-8') as a:
    b = a.readlines()

    for i in b:
        for j in i.replace('\n', ''):
            first = (ord(j) - 44032) // 588
            second = ((ord(j) - 44032) % 588) // 28
            third = ((ord(j) - 44032) % 588) % 28

            result += chr(first + 4352) + chr(second + 4449)
            result += chr(third + 4519) if third != 0 else ''
        result += '\n'

with open('new.txt', mode='w', encoding='utf-8') as a:
    a.write(result)'''

'''
16진수
초성: 1100(ㄱ) ~ 1112(ㅎ)
중성: 1161(ㅏ) ~ 1175(ㅣ)
종성: 11A8(ㄱ) ~ 11C2(ㅎ)

10진수
초성: 4352(ㄱ) ~ 4370(ㅎ)
중성: 4449(ㅏ) ~ 4469(ㅣ)
종성: 4520(ㄱ) ~ 4546(ㅎ)


16진수
3131(ㄱ) ~ 314E(ㅎ)
314F(ㅏ) ~ 3163(ㅣ)

10진수
12593(ㄱ) ~ 12622(ㅎ)
12623(ㅏ) ~ 12643(ㅣ)
'''

JAUEM = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅄ',
         'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JAUEM_SEP = ['ㄱ', ('ㄱ', 'ㄱ'), ('ㄱ', 'ㅅ'), 'ㄴ', ('ㄴ', 'ㅈ'), ('ㄴ', 'ㅎ'), 'ㄷ', ('ㄷ', 'ㄷ'), 'ㄹ', ('ㄹ', 'ㄱ'), ('ㄹ', 'ㅁ'),
             ('ㄹ', 'ㅂ'), ('ㄹ', 'ㅅ'), ('ㄹ', 'ㅌ'), ('ㄹ', 'ㅍ'), ('ㄹ', 'ㅎ'), 'ㅁ', 'ㅂ', ('ㅂ', 'ㅂ'), ('ㅂ', 'ㅅ'),
             'ㅅ', ('ㅅ', 'ㅅ'), 'ㅇ', 'ㅈ', ('ㅈ', 'ㅈ'), 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

MOUEM = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
MOUEM_SEP = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', ('ㅗ', 'ㅏ'), ('ㅗ', 'ㅐ'), ('ㅗ', 'ㅣ'), 'ㅛ',
             'ㅜ', ('ㅜ', 'ㅓ'), ('ㅜ', 'ㅔ'), ('ㅜ', 'ㅣ'), 'ㅠ', 'ㅡ', ('ㅡ', 'ㅣ'), 'ㅣ']

CHOSEONG = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
CHOSEONG_SEP = ['ㄱ', ('ㄱ', 'ㄱ'), 'ㄴ', 'ㄷ', ('ㄷ', 'ㄷ'), 'ㄹ', 'ㅁ', 'ㅂ', ('ㅂ', 'ㅂ'), ('ㅅ', 'ㅅ'), 'ㅇ', 'ㅈ',
                ('ㅈ', 'ㅈ'), 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

JONGSEONG = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅆ',
             'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JONGSEONG_SEP = ['ㄱ', ('ㄱ', 'ㄱ'), ('ㄱ', 'ㅅ'), 'ㄴ', ('ㄴ', 'ㅈ'), ('ㄴ', 'ㅎ'), 'ㄷ', 'ㄹ', ('ㄹ', 'ㄱ'), ('ㄹ', 'ㅁ'),
                 ('ㄹ', 'ㅂ'), ('ㄹ', 'ㅅ'), ('ㄹ', 'ㅌ'), ('ㄹ', 'ㅍ'), ('ㄹ', 'ㅎ'), 'ㅁ', 'ㅂ', 'ㅅ', ('ㅅ', 'ㅅ'),
                 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


def normalization(iterable, no_sep_stacked):
    for char in iterable:
        if ord(char) in [4352, 4520]:
            yield 'ㄱ'
        elif ord(char) in [4353, 4521]:
            yield 'ㄲ' if no_sep_stacked else 'ㄱ', 'ㄱ'
        elif ord(char) in [4522]:
            yield 'ㄳ' if no_sep_stacked else 'ㄱ', 'ㅅ'
        elif ord(char) in [4354, 4523]:
            yield 'ㄴ'
        elif ord(char) in [4524]:
            yield 'ㄵ' if no_sep_stacked else 'ㄴ', 'ㅈ'
        elif ord(char) in [4525]:
            yield 'ㄶ' if no_sep_stacked else 'ㄴ', 'ㅎ'
        elif ord(char) in [4355, 4526]:
            yield 'ㄷ'
        elif ord(char) in [4356]:
            yield 'ㄸ' if no_sep_stacked else 'ㄷ', 'ㄷ'
        elif ord(char) in [4357, 4527]:
            yield 'ㄹ'
        elif ord(char) in [4528]:
            yield 'ㄺ' if no_sep_stacked else 'ㄹ', 'ㄱ'
        elif ord(char) in [4529]:
            yield 'ㄻ' if no_sep_stacked else 'ㄹ', 'ㅁ'
        elif ord(char) in [4530]:
            yield 'ㄼ' if no_sep_stacked else 'ㄹ', 'ㅂ'
        elif ord(char) in [4531]:
            yield 'ㄽ' if no_sep_stacked else 'ㄹ', 'ㅅ'
        elif ord(char) in [4532]:
            yield 'ㄾ' if no_sep_stacked else 'ㄹ', 'ㅌ'
        elif ord(char) in [4533]:
            yield 'ㄿ' if no_sep_stacked else 'ㄹ', 'ㅍ'
        elif ord(char) in [4534]:
            yield 'ㅀ' if no_sep_stacked else 'ㄹ', 'ㅎ'
        elif ord(char) in [4358, 4535]:
            yield 'ㅁ'
        elif ord(char) in [4359, 4536]:
            yield 'ㅂ'
        elif ord(char) in [4360]:
            yield 'ㅃ' if no_sep_stacked else 'ㅂ', 'ㅂ'
        elif ord(char) in [4537]:
            yield 'ㅄ' if no_sep_stacked else 'ㅂ', 'ㅅ'
        elif ord(char) in [4361, 4538]:
            yield 'ㅅ'
        elif ord(char) in [4362, 4539]:
            yield 'ㅆ' if no_sep_stacked else 'ㅅ', 'ㅅ'
        elif ord(char) in [4363, 4540]:
            yield 'ㅇ'
        elif ord(char) in [4364, 4541]:
            yield 'ㅈ'
        elif ord(char) in [4365]:
            yield 'ㅉ' if no_sep_stacked else 'ㅈ', 'ㅈ'
        elif ord(char) in [4366, 4542]:
            yield 'ㅊ'
        elif ord(char) in [4367, 4543]:
            yield 'ㅋ'
        elif ord(char) in [4368, 4544]:
            yield 'ㅌ'
        elif ord(char) in [4369, 4545]:
            yield 'ㅍ'
        elif ord(char) in [4370, 4546]:
            yield 'ㅎ'
        elif ord(char) == 4449:
            yield 'ㅏ'
        elif ord(char) == 4450:
            yield 'ㅐ'
        elif ord(char) == 4451:
            yield 'ㅑ'
        elif ord(char) == 4452:
            yield 'ㅒ'
        elif ord(char) == 4453:
            yield 'ㅓ'
        elif ord(char) == 4454:
            yield 'ㅔ'
        elif ord(char) == 4455:
            yield 'ㅕ'
        elif ord(char) == 4456:
            yield 'ㅖ'
        elif ord(char) == 4457:
            yield 'ㅗ'
        elif ord(char) == 4458:
            yield 'ㅘ' if no_sep_stacked else 'ㅗ', 'ㅏ'
        elif ord(char) == 4459:
            yield 'ㅙ' if no_sep_stacked else 'ㅗ', 'ㅐ'
        elif ord(char) == 4460:
            yield 'ㅚ' if no_sep_stacked else 'ㅗ', 'ㅣ'
        elif ord(char) == 4461:
            yield 'ㅛ'
        elif ord(char) == 4462:
            yield 'ㅜ'
        elif ord(char) == 4463:
            yield 'ㅝ' if no_sep_stacked else 'ㅜ', 'ㅓ'
        elif ord(char) == 4464:
            yield 'ㅞ' if no_sep_stacked else 'ㅜ', 'ㅔ'
        elif ord(char) == 4465:
            yield 'ㅟ' if no_sep_stacked else 'ㅜ', 'ㅣ'
        elif ord(char) == 4466:
            yield 'ㅠ'
        elif ord(char) == 4467:
            yield 'ㅡ'
        elif ord(char) == 4468:
            yield 'ㅢ' if no_sep_stacked else 'ㅡ', 'ㅣ'
        else:
            yield 'ㅣ'


class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi('gui.ui', self)
        self.ui.show()

        self.LABELS_JAUEM = [self.jauem_1, self.jauem_2, self.jauem_3, self.jauem_4, self.jauem_5,
                             self.jauem_6, self.jauem_7, self.jauem_8, self.jauem_9, self.jauem_10]
        self.LABELS_MOUEM = [self.mouem_1, self.mouem_2, self.mouem_3, self.mouem_4, self.mouem_5,
                             self.mouem_6, self.mouem_7, self.mouem_8]

        self.LABELS_JA_COUNT = [self.ja_count_1, self.ja_count_2, self.ja_count_3, self.ja_count_4, self.ja_count_5,
                                self.ja_count_6, self.ja_count_7, self.ja_count_8, self.ja_count_9, self.ja_count_10]
        self.LABELS_MO_COUNT = [self.mo_count_1, self.mo_count_2, self.mo_count_3, self.mo_count_4, self.mo_count_5,
                                self.mo_count_6, self.mo_count_7, self.mo_count_8]
        # self.LABELS_WORD[몇 번째][초/중/종][위치(중/종만)]
        self.LABELS_WORD = [{"cho": self.cho_1, "jung": {"right": self.jungr_1, "bottom": self.jungb_1},
                             "jong": {"top_right": self.jongtr_1, "bottom_left": self.jongbl_1,
                                      "bottom_right": self.jongbr_1}},
                            {"cho": self.cho_2, "jung": {"right": self.jungr_2, "bottom": self.jungb_2},
                             "jong": {"top_right": self.jongtr_2, "bottom_left": self.jongbl_2,
                                      "bottom_right": self.jongbr_2}},
                            {"cho": self.cho_3, "jung": {"right": self.jungr_3, "bottom": self.jungb_3},
                             "jong": {"top_right": self.jongtr_3, "bottom_left": self.jongbl_3,
                                      "bottom_right": self.jongbr_3}},
                            {"cho": self.cho_4, "jung": {"right": self.jungr_4, "bottom": self.jungb_4},
                             "jong": {"top_right": self.jongtr_4, "bottom_left": self.jongbl_4,
                                      "bottom_right": self.jongbr_4}},
                            {"cho": self.cho_5, "jung": {"right": self.jungr_5, "bottom": self.jungb_5},
                             "jong": {"top_right": self.jongtr_5, "bottom_left": self.jongbl_5,
                                      "bottom_right": self.jongbr_5}},
                            {"cho": self.cho_6, "jung": {"right": self.jungr_6, "bottom": self.jungb_6},
                             "jong": {"top_right": self.jongtr_6, "bottom_left": self.jongbl_6,
                                      "bottom_right": self.jongbr_6}}]

        self.words = []
        self.jamo = {}
        self.cur_jamo = {}

        self.input = ""
        self.words_found = []

        self.no_shift = True

        with open('words.txt', encoding='utf-8') as words_file:
            self.WORDS = list(map(lambda x: x.replace('\n', ''), words_file.readlines()))
        with open('sep_words.txt', encoding='utf-8') as sep_words_file:
            self.SEP_WORDS = list(map(lambda x: x.replace('\n', ''), sep_words_file.readlines()))
        with open('norm_sep_words.txt', encoding='utf-8') as norm_sep_file:
            self.NORMALIZED_SEP_WORDS = list(map(lambda x: x.replace('\n', ''), norm_sep_file.readlines()))

        self.game_setting()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Shift:
            self.no_shift = False
        elif e.key() == QtCore.Qt.Key_Backspace:
            if self.input:
                if self.input[-1] == "ㄲ":
                    self.cur_jamo['ㄱ'] += 2
                elif self.input[-1] == "ㄸ":
                    self.cur_jamo['ㄷ'] += 2
                elif self.input[-1] == "ㅃ":
                    self.cur_jamo['ㅂ'] += 2
                elif self.input[-1] == "ㅆ":
                    self.cur_jamo['ㅅ'] += 2
                elif self.input[-1] == "ㅉ":
                    self.cur_jamo['ㅈ'] += 2
                else:
                    self.cur_jamo[self.input[-1]] += 1
                self.input = self.input[:-1]
                self.display_update()
        elif e.key() == QtCore.Qt.Key_Return or e.key() == QtCore.Qt.Key_Enter:
            self.word_check()

        elif e.key() == QtCore.Qt.Key_R:
            self.input_valid('ㄱ') if self.no_shift else self.input_valid('ㄲ')
        elif e.key() == QtCore.Qt.Key_S:
            self.input_valid('ㄴ')
        elif e.key() == QtCore.Qt.Key_E:
            self.input_valid('ㄷ') if self.no_shift else self.input_valid('ㄸ')
        elif e.key() == QtCore.Qt.Key_F:
            self.input_valid('ㄹ')
        elif e.key() == QtCore.Qt.Key_A:
            self.input_valid('ㅁ')
        elif e.key() == QtCore.Qt.Key_Q:
            self.input_valid('ㅂ') if self.no_shift else self.input_valid('ㅃ')
        elif e.key() == QtCore.Qt.Key_T:
            self.input_valid('ㅅ') if self.no_shift else self.input_valid('ㅆ')
        elif e.key() == QtCore.Qt.Key_D:
            self.input_valid('ㅇ')
        elif e.key() == QtCore.Qt.Key_W:
            self.input_valid('ㅈ') if self.no_shift else self.input_valid('ㅉ')
        elif e.key() == QtCore.Qt.Key_C:
            self.input_valid('ㅊ')
        elif e.key() == QtCore.Qt.Key_Z:
            self.input_valid('ㅋ')
        elif e.key() == QtCore.Qt.Key_X:
            self.input_valid('ㅌ')
        elif e.key() == QtCore.Qt.Key_V:
            self.input_valid('ㅍ')
        elif e.key() == QtCore.Qt.Key_G:
            self.input_valid('ㅎ')
        elif e.key() == QtCore.Qt.Key_K:
            self.input_valid('ㅏ')
        elif e.key() == QtCore.Qt.Key_O:
            self.input_valid('ㅐ') if self.no_shift else self.input_valid('ㅒ')
        elif e.key() == QtCore.Qt.Key_I:
            self.input_valid('ㅑ')
        elif e.key() == QtCore.Qt.Key_J:
            self.input_valid('ㅓ')
        elif e.key() == QtCore.Qt.Key_P:
            self.input_valid('ㅔ') if self.no_shift else self.input_valid('ㅖ')
        elif e.key() == QtCore.Qt.Key_U:
            self.input_valid('ㅕ')
        elif e.key() == QtCore.Qt.Key_H:
            self.input_valid('ㅗ')
        elif e.key() == QtCore.Qt.Key_Y:
            self.input_valid('ㅛ')
        elif e.key() == QtCore.Qt.Key_N:
            self.input_valid('ㅜ')
        elif e.key() == QtCore.Qt.Key_B:
            self.input_valid('ㅠ')
        elif e.key() == QtCore.Qt.Key_M:
            self.input_valid('ㅡ')
        elif e.key() == QtCore.Qt.Key_L:
            self.input_valid('ㅣ')

    def keyReleaseEvent(self, e):
        if e.key() == QtCore.Qt.Key_Shift:
            self.no_shift = True

    def game_setting(self):
        self.choose_words()
        self.display_update()
        print(self.words)

    def choose_words(self):
        while True:  # 5~10 단어를 골라서 자모 18개 이하로 이뤄져 있고 6글자 이하이면 통과
            word_number = rd.randint(5, 10)
            temp = rd.choices(self.SEP_WORDS, k=word_number)
            if len(temp) != len(set(temp)):  # 중복 검사
                continue

            if not all(list(map(lambda x: True if len(x) <= 6 else False, temp))):  # 글자 수 검사
                continue

            temp_jamo = list(it.chain.from_iterable(normalization(it.chain.from_iterable(temp), False)))
            if len(set(temp_jamo)) <= 18:  # 총 자모 수 검사
                self.words = temp
                for char in temp_jamo:  # 자모음 딕셔너리 생성
                    if char in self.jamo.keys():
                        self.jamo[char] += 1
                    else:
                        self.jamo[char] = 1

                self.cur_jamo = self.jamo.copy()
                sep_jamo = self.sep_jamo()
                if len(sep_jamo["ja"].keys()) > 10 or len(sep_jamo["mo"].keys()) > 8:  # 자음 10개, 모음 8개 이하
                    self.jamo.clear()
                    continue
                break

    def input_valid(self, char):
        if char == 'ㄲ':
            key_check = 'ㄱ'
            count = 2
        elif char == 'ㄸ':
            key_check = 'ㄷ'
            count = 2
        elif char == 'ㅃ':
            key_check = 'ㅂ'
            count = 2
        elif char == 'ㅆ':
            key_check = 'ㅅ'
            count = 2
        elif char == 'ㅉ':
            key_check = 'ㅈ'
            count = 2
        else:
            key_check = char
            count = 1

        if key_check in self.cur_jamo.keys() and self.cur_jamo[key_check] >= count:
            self.input += char
            self.cur_jamo[key_check] -= count
            self.display_update()
        else:
            pass  # 잘못 입력

    def display_update(self):
        # 자모음 리스트
        sep_jamo = self.sep_jamo()
        num = 0
        for key in sep_jamo["ja"].keys():
            pixmap = QtGui.QPixmap("./JaUem/" + key + ".png").scaled(80, 80)
            self.LABELS_JAUEM[num].setPixmap(pixmap)
            num += 1
        num = 0
        for value in sep_jamo["ja"].values():
            self.LABELS_JA_COUNT[num].setText(str(value))
            num += 1

        num = 0
        for key in sep_jamo["mo"].keys():
            pixmap = QtGui.QPixmap("./MoUem/" + key + ".png").scaled(80, 80)
            self.LABELS_MOUEM[num].setPixmap(pixmap)
            num += 1
        num = 0
        for value in sep_jamo["mo"].values():
            self.LABELS_MO_COUNT[num].setText(str(value))
            num += 1

        # 사용자 입력
        for i in self.LABELS_WORD:
            i['cho'].setPixmap(QtGui.QPixmap(''))
            for j in i['jung'].values():
                j.setPixmap(QtGui.QPixmap(''))
            for j in i['jong'].values():
                j.setPixmap(QtGui.QPixmap(''))

        num = 0
        letter = 0
        words = [{"cho": '', "jung": '', "jung2": '', "jong": ''}, {"cho": '', "jung": '', "jung2": '', "jong": ''},
                 {"cho": '', "jung": '', "jung2": '', "jong": ''}, {"cho": '', "jung": '', "jung2": '', "jong": ''},
                 {"cho": '', "jung": '', "jung2": '', "jong": ''}, {"cho": '', "jung": '', "jung2": '', "jong": ''}]
        is_ja_l = list(map(lambda x: True if ord(x) <= 12622 else False, self.input))

        error = True
        for char, is_ja in zip(self.input, is_ja_l):
            try:
                # 자음일 때
                if is_ja:
                    # 맨 처음이면
                    if num == 0:
                        # 첫 글자 초성으로 설정
                        words[0]["cho"] = char

                    # 맨 처음이 아니면
                    else:
                        # 앞 캐릭터가 자음이면
                        if is_ja_l[num - 1]:
                            # 앞 글자의 종성이 있으면
                            if words[letter - 1]['jong']:
                                # 앞 캐릭터와 합쳐질 수 있으면
                                if (self.input[num - 1], char) in JONGSEONG_SEP:
                                    # 마지막 캐릭터이거나 뒤 캐릭터가 자음이면
                                    if len(self.input) == num + 1 or is_ja_l[num + 1]:
                                        # 앞 글자의 종성으로 합침
                                        words[letter - 1]['jong'] = JONGSEONG[JONGSEONG_SEP.index((self.input[num - 1],
                                                                                                   char))]

                                    # 뒤 캐릭터가 모음이면
                                    else:
                                        # 현재 글자의 초성으로 설정
                                        words[letter]['cho'] = char

                                # 앞 캐릭터와 합쳐질 수 없으면
                                else:
                                    # 마지막 캐릭터이거나 뒤 캐릭터가 모음이면
                                    if len(self.input) == num + 1 or not is_ja_l[num + 1]:
                                        # 현재 글자의 초성으로 설정
                                        words[letter]['cho'] = char

                                    # 뒤 캐릭터가 자음이면
                                    else:
                                        # 에러
                                        break

                            # 앞 글자의 종성이 없으면
                            else:
                                # 에러
                                break

                        # 앞 캐릭터가 모음이면
                        else:
                            # 종성에 올 수 있으면
                            if char in JONGSEONG:
                                # 현재 글자의 종성으로 설정
                                words[letter]['jong'] = char
                                letter += 1

                            # 종성에 올 수 없으면
                            else:
                                # 뒤 글자의 종성으로 설정
                                letter += 1
                                words[letter]['cho'] = char

                # 모음일 때
                else:
                    # 맨 처음이면
                    if num == 0:
                        # 에러
                        break

                    # 맨 처음이 아니면
                    else:
                        # 현재 글자의 중성이 없으면
                        if not words[letter]['jung']:
                            # 현재 글자의 초성이 있으면
                            if words[letter]['cho']:
                                # 현재 글자의 중성으로 설정
                                words[letter]['jung'] = char

                            # 현재 글자의 초성이 없으면
                            else:
                                # 앞 글자의 종성이 있으면
                                if words[letter - 1]['jong']:
                                    # 앞 글자의 종성이 합용 병서이면
                                    if words[letter - 1]['jong'] in "ㄳㄵㄶㄺㄻㄼㄽㄾㄿㅀㅄ":
                                        # 앞 글자의 종성과 현재 글자의 초성으로 나눈 후 현재 글자의 중성으로 설정
                                        jong_l = JONGSEONG_SEP[JONGSEONG.index(words[letter]['jong'])][0]
                                        words[letter - 1]['jong'] = jong_l[0]
                                        words[letter]['cho'] = jong_l[1]
                                        words[letter]['jung'] = char

                                    # 앞 글자의 종성이 겹받침이 아니면
                                    else:
                                        # 앞 글자의 종성을 없애고 현재 글자의 초성으로 설정 후 현재 글자의 중성으로 설정
                                        words[letter]['cho'] = words[letter - 1]['jong']
                                        words[letter - 1]['jong'] = ''
                                        words[letter]['jung'] = char

                                # 앞 글자의 종성이 없으면
                                else:
                                    # 에러
                                    break

                        # 현재 글자의 중성이 하나 있으면
                        elif words[letter]['jung'] and not words[letter]['jung2']:
                            # 현재 글자의 중성과 합쳐지면
                            if (words[letter]['jung'], char) in MOUEM_SEP:
                                # 현재 글자의 두 번째 중성으로 설정
                                words[letter]['jung2'] = char

                            # 현재 글자의 중성과 합쳐지지 않으면
                            else:
                                # 에러
                                break

                        # 현재 글자의 중성이 두 개 있으면
                        else:
                            # 에러
                            break

                num += 1

            except IndexError:  # 6글자를 넘어가면 에러
                break
        else:
            error = False

        num = 0
        for letter in words:
            if letter['cho']:
                self.LABELS_WORD[num]['cho'].setPixmap(QtGui.QPixmap(
                    './JaUem/' + letter['cho'] + '.png').scaled(80, 80))

            if letter['jung']:
                if letter['jung2']:
                    self.LABELS_WORD[num]['jung']['bottom'].setPixmap(QtGui.QPixmap(
                        './MoUem/' + letter['jung'] + '.png').scaled(80, 80))
                    self.LABELS_WORD[num]['jung']['right'].setPixmap(QtGui.QPixmap(
                        './MoUem/' + letter['jung2'] + '.png').scaled(80, 80))
                    if letter['jong']:
                        self.LABELS_WORD[num]['jong']['bottom_right'].setPixmap(QtGui.QPixmap(
                            './JaUem/' + letter['jong'] + '.png').scaled(80, 80))
                else:
                    if letter['jung'] in "ㅏㅐㅑㅒㅓㅔㅕㅖㅣ":
                        self.LABELS_WORD[num]['jung']['right'].setPixmap(QtGui.QPixmap(
                            './MoUem/' + letter['jung'] + '.png').scaled(80, 80))
                        if letter['jong']:
                            self.LABELS_WORD[num]['jong']['top_right'].setPixmap(QtGui.QPixmap(
                                './JaUem/' + letter['jong'] + '.png').scaled(80, 80))
                    else:
                        self.LABELS_WORD[num]['jung']['bottom'].setPixmap(QtGui.QPixmap(
                            './MoUem/' + letter['jung'] + '.png').scaled(80, 80))
                        if letter['jong']:
                            self.LABELS_WORD[num]['jong']['bottom_left'].setPixmap(QtGui.QPixmap(
                                './JaUem/' + letter['jong'] + '.png').scaled(80, 80))
            num += 1

        if error:
            self.input_reset()

    def input_reset(self):
        self.input = ""
        self.cur_jamo = self.jamo.copy()
        self.display_update()

    def word_check(self):
        norm_input = self.input.replace("ㄲ", 'ㄱㄱ').replace("ㄸ", 'ㄷㄷ').replace("ㅃ", 'ㅂㅂ')\
            .replace("ㅆ", 'ㅅㅅ').replace("ㅉ", 'ㅈㅈ')

        if self.input in self.words_found:  # 중복
            pass
        else:
            if norm_input in self.NORMALIZED_SEP_WORDS:
                if norm_input in map(lambda x: ''.join(it.chain.from_iterable(normalization(x, False))), self.words):
                    self.key_words.append(self.WORDS[self.NORMALIZED_SEP_WORDS.index(norm_input)])
                else:  # Other Words
                    self.other_words.append(self.WORDS[self.NORMALIZED_SEP_WORDS.index(norm_input)])

                self.words_found.append(self.input)
                if len(self.words_found) == len(self.words):  # All Key Words Found
                    self.game_win()
            else:
                pass  # no word
        self.input_reset()

    def sep_jamo(self):
        is_ja = list(map(lambda x: True if ord(x) <= 12622 else False, self.cur_jamo.keys()))
        ja = dict(zip(it.compress(self.cur_jamo.keys(), is_ja),
                      it.compress(self.cur_jamo.values(), is_ja)))
        mo = dict(zip(it.compress(self.cur_jamo.keys(), list(map(lambda x: not x, is_ja))),
                      it.compress(self.cur_jamo.values(), list(map(lambda x: not x, is_ja)))))
        return {"ja": ja, "mo": mo}

    def game_win(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = MainWindow(None)
    p = Window.palette()
    p.setColor(Window.backgroundRole(), QtGui.QColor(189, 189, 189))
    Window.setPalette(p)
    Window.show()
    app.exec_()
    Window.choose_words()
