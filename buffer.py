class Buffer:
    def load_file(self, file_path):
        file = open(file_path, "r")
        text = file.readline()

        buffer = []
        count = 1

        while text != "":
            buffer.append(text)
            text = file.readline()
            count += 1

            if count == 10 or text == "":
                buf = ''.join(buffer)
                count = 1
                yield buf

                buffer = []

        file.close()
