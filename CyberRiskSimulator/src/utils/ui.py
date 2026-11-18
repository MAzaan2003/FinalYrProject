from colorama import init, Fore, Style

init(autoreset=True)


def banner():

    print(Fore.CYAN + Style.BRIGHT + r"""
   _____      _                _____     _     _
  / ____|    | |              |  __ \   (_)   | |
 | |     _ __| |__   ___ _ __ | |__) |___ _ ___| | __
 | |    | '__| '_ \ / _ \ '__||  _  // _ \ / __| |/ /
 | |____| |  | |_) |  __/ |   | | \ \  __/ \__ \   <
  \_____|_|  |_.__/ \___|_|   |_|  \_\___|_|___/_|\_\

              CYBER RISK SIMULATOR
    """)



def line():

    print(Fore.CYAN + "=" * 70)



def success(message):

    print(Fore.GREEN + "✔ " + message)



def warning(message):

    print(Fore.YELLOW + "⚠ " + message)



def error(message):

    print(Fore.RED + "✖ " + message)



def title(message):

    line()

    print(
        Fore.CYAN +
        Style.BRIGHT +
        message.center(70)
    )

    line()