def using_control_once() -> str:
    if 9 > 8 :
        return "Success #1"


def using_control_again() -> str:
    if 9 == 9:
        return "Success #2"


print(using_control_once())
print(using_control_again())
