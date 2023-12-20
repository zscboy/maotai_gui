# Source Generated with Decompyle++
# File: ModifiedBase64.pyc (Python 3.9)


class ModifiedBase64(object):
    def __init__(self):
        self.aae = [
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "a",
            "b",
            "c",
            "d",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "y",
            "z",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "+",
            "/",
        ]
        self.aaf = [None] * 128
        i = 0
        i2 = 0
        bArr = self.aaf
        while i2 <= len(bArr) - 1:
            bArr[i2] = -1
            i2 += 1

        cArr = self.aae
        while i <= len(cArr) - 1:
            self.aaf[ord(cArr[i])] = int(i)
            i += 1

        return None

    def m23207r(self, str_):
        result = ""
        bArr = bytearray(str_.encode("utf-8"))
        i = 0
        while i <= len(bArr) - 1:
            bArr2 = [None] * 4
            b = 0
            i2 = 0
            if i2 <= 2:
                i3 = i + i2
                if i3 <= len(bArr) - 1:
                    bArr2[i2] = b | (bArr[i3] & 255) >> i2 * 2 + 2
                    b = ((bArr[i3] & 255) << (2 - i2) * 2 + 2 & 255) >> 2
                else:
                    bArr2[i2] = b
                    b = 64
                i2 += 1

            bArr2[3] = b
            i4 = 0
            while i4 <= 3:
                if bArr2[i4] <= 63:
                    result = result + self.aae[bArr2[i4]]
                else:
                    result = result + "="
                i4 += 1

            i += 3

        return result

    def m23209eC(self, str_):
        """generated source for method m23209eC"""
        bys = []
        bytes = bytearray(str_.encode("utf-8"))
        bArr = [None] * len(bytes)
        i = 0
        while i <= len(bytes) - 1:
            bArr[i] = self.aaf[bytes[i]]
            i += 1

        i2 = 0
        while i2 <= len(bArr) - 1:
            bArr2 = [None] * 3
            i3 = 0
            i4 = 0
            i7 = 0
            while i4 <= 2:
                i5 = i2 + i4
                i6 = i5 + 1
                if i6 <= len(bArr) and bArr[i6] >= 0:
                    bArr2[i4] = (bArr[i5] & 255) << i4 * 2 + 2 | (bArr[i6] & 255) >> (
                        2 - i4 + 1
                    ) * 2 + 2
                    i3 += 1
                i4 += 1

            while i7 <= i3 - 1:
                bys.append(self.py2ja(bArr2[i7]))
                i7 += 1

            i2 += 4

        return bytearray(bys).decode("utf-8")

    def py2ja(self=None, arr=None):
        """
        python字节数组转java字节数组
        :return:
        """
        while arr >= 256:
            arr = arr - 256

        return arr


if __name__ == "__main__":
    v = ModifiedBase64()
    text = "5ZIG5Ya26AQX6YQJ5YsY6SML5bsS"
    text = "唐冶街道刘老师"
