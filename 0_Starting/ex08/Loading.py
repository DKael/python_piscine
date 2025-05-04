# import time
# import shutil


# def time_format(second: int):
#     """
#     Convert seconds to formatted time string.
#     """
#     second = int(second)
#     h = second // 3600
#     second = second % 3600
#     m = second // 60
#     s = second % 60
#     if h > 0:
#         return f"{h}:{m:02d}:{s:02d}"
#     else:
#         return f"{m:02d}:{s:02d}"


def ft_tqdm(lst: range) -> None:
    """

    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.

    Parameters
    ----------
    iterable  : iterable
        Iterable to decorate with a progressbar.
        Leave blank to manually manage the updates.

    Returns
    -------
    out  : decorated iterator.
    """
    total = len(lst)
    # start_time = time.time()
    # output_width = shutil.get_terminal_size().columns
    output_width = 80

    for idx, item in enumerate(lst, start=1):
        percentage = idx / float(total)
        percentage_str = f"{int(percentage * 100):>3d}%"

        detail_str = f"{idx}/{total}"

        # elapsed_time = time.time() - start_time
        # speed = idx / elapsed_time
        # etd = (total - idx) / speed

        # time_str = f"{time_format(elapsed_time)}<{time_format(etd)}"
        # speed_str = f"{speed:>6.2f}it/s"

        # info = f" {detail_str} [{time_str},{speed_str}]"
        info = f" {detail_str}"

        bar_size = output_width - len(percentage_str) - 2 - len(info)
        bar_str = f"|{'█' * int(bar_size * percentage):<{bar_size}}|"
        print(f"\r{percentage_str}{bar_str}{info}", end="", flush=True)
        yield item
    print()
