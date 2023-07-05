class before:
    pass


class inbetween:
    pass


class after:
    pass


VERSION = "1.0.1"
AUTHOR = "GrenManSK"


class get_logger:
    def __init__(self, strict: bool = True, quiet=False):
        self.level = 0
        self.start = True
        self.strict = strict
        self.quiet = quiet

    def next(
        self,
        text: str = "",
        end: str = "\n",
        by: int = 1,
        toprint: bool = True,
        where: after | before | inbetween = after,
    ):
        if self.quiet:
            toprint = False
        self.level += by
        start = False
        if self.start:
            start = True
            if toprint:
                if where is before:
                    print(f"|{text}")
                    print("|_______________________________________")
                elif where is inbetween:
                    print(
                        f"|{'____'*(self.level-by)}_______________________________________{text}"
                    )
                    return f"|{'____'*(self.level-by)}_______________________________________{text}"
                else:
                    print(
                        f"|{'____'*(self.level-by)}____________________________________________________"
                    )
            self.start = False
        else:
            if toprint:
                if where is before:
                    print(f"{(self.level - by)*'    '}|{text}")
                    print(
                        f"{'____'*(self.level - by)}|_______________________________________"
                    )
                else:
                    print(
                        f"{'____'*(self.level-by)}|____________________________________________________"
                    )
        message = f"{self.level*'    '}|{text}" + end
        if toprint and where is after:
            print(f"{self.level*'    '}|{text}", end=end)
        if start:
            return (
                f"|{'____'*(self.level-by)}____________________________________________________\n"
                + message
            )
        else:
            return message

    def prev(
        self,
        text: str = "",
        end: str = "\n",
        by: int = 1,
        toprint: bool = True,
        where: after | before | inbetween = after,
    ):
        if self.quiet:
            toprint = False
        if self.level == 0:
            if self.strict:
                raise RuntimeError("Can not go under the current level")
            else:
                return "Can not go under the current level"
        self.level -= by
        if toprint:
            if where is before:
                print(f"{(self.level + by)*'    '}|{text}")
                print(
                    f"{(self.level + by)*'____'}|_______________________________________"
                )
            elif where is inbetween:
                print(
                    f"{'____'*(self.level+by)}|_______________________________________{text}"
                )
                return f"{'____'*(self.level+by)}|_______________________________________{text}"
            else:
                print(
                    f"{'____'*(self.level+by)}|____________________________________________________"
                )
        if self.level == 0:
            self.start = True
            message = f"|{self.level*'    '}{text}"
            if toprint and where is after:
                print(f"|{self.level*'    '}{text}", end=end)
            return message + end
        else:
            message = f"{self.level*'    '}|{text}"
            if toprint and where is after:
                print(f"{self.level*'    '}|{text}", end=end)
            return message + end

    def stay(self, text: str = "", end: str = "\n", toprint: bool = True):
        if self.quiet:
            toprint = False
        if toprint:
            print(f"{self.level*'    '}|{text}", end=end)
        return f"{self.level*'    '}|{text}" + end
