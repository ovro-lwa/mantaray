import requests
import time
import functools

"""
this acutally does not work.
"""
def daily_at_hr(hour, day=None):
    def dec(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ts = time.localtime()
            if ts.tm_hour == hour and ((day is None) or (day != ts.tm_mday)):
                func(*args, **kwargs)
                return daily_at_hr(hour, day=ts.tm_mday)(func)
            else:
                return daily_at_hr(hour, day=day)(func)
        return wrapper 
    return dec

@daily_at_hr(4)
def weeeeeeeee():
    print('its 4 oclock.')
    requests.post("https://ntfy.sh/ovro-lwa-manta-ray-says", 
                    data="""
                            ⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠹⣿⣷⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⢀⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣷⣶⣶⣿⣧⠀⠀⠀⠀⢀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⡇⢸⣇⠘⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣠⠟⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣷⠈⢿⣦⣘⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣷⣄⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠙⢿⣦⣄⣉⣹⣿⣿⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣌⣉⣉⣿⣿⣿⣧⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⣤⣴⠾⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀
    ⠀⠀⠀⢀⣾⠛⠉⠀⠀⠀⠙⠛⠛⠛⠛⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀
    ⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⣿⣿⣿⣇⠀⠀
    ⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⡀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀
                    """.encode(encoding='utf-8'))

if __name__ == '__main__':
    while True:
        # or, maybe, processes and notify and stuff.
        # or, like, run a shell script.
        weeeeeeeee()
        time.sleep(10)