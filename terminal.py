from datetime import datetime

import gifos


def main():
    t = gifos.Terminal(750, 420, 15, 15)
    year_now = datetime.now().strftime("%Y")

    t.gen_text("", 1, count=15)
    t.toggle_show_cursor(False)
    t.gen_text("BIOS v2.0.24 - System Boot", 1)
    t.gen_text(f"Copyright (C) {year_now}, \x1b[96mIvan Industries\x1b[0m", 2)
    t.gen_text("Krypton(tm) GIFCPU - 500Hz", 4)
    t.gen_text(
        "Press \x1b[94mDEL\x1b[0m to enter SETUP, "
        "\x1b[94mESC\x1b[0m to cancel Memory Test",
        t.num_rows,
    )
    for i in range(0, 65653, 14336):
        t.delete_row(5)
        t.gen_text(f"Memory Test: {i}", 5, contin=True)
    t.delete_row(5)
    t.gen_text("Memory Test: 64KB OK", 5, count=8, contin=True)
    t.gen_text("", 7, count=8, contin=True)

    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)

    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mGIF OS v2.0.24 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("IvanWng97", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("**********", 4, contin=True)
    t.toggle_show_cursor(False)
    time_now = datetime.now().strftime("%a %b %d %I:%M:%S %p %Y")
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    t.gen_prompt(8, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[92mneofetch\x1b[0m", 8, contin=True)

    stats = gifos.utils.fetch_github_stats("IvanWng97")
    top_langs = [lang[0] for lang in stats.languages_sorted[:5]]

    t.clear_frame()
    details = f"""\
    \x1b[30;106m IvanWng97@GitHub \x1b[0m
    -------------------
    \x1b[96mOS:      \x1b[93mmacOS Darwin\x1b[0m
    \x1b[96mShell:   \x1b[93mzsh / fish\x1b[0m
    \x1b[96mEditor:  \x1b[93mNeovim\x1b[0m
    \x1b[96mLangs:   \x1b[93m{', '.join(top_langs)}\x1b[0m

    \x1b[30;106m GitHub Stats \x1b[0m
    -------------------
    \x1b[96mRank:    \x1b[93m{stats.user_rank.level}\x1b[0m
    \x1b[96mStars:   \x1b[93m{stats.total_stargazers}\x1b[0m
    \x1b[96mCommits: \x1b[93m{stats.total_commits_last_year}\x1b[0m
    \x1b[96mPRs:     \x1b[93m{stats.total_pull_requests_made}\x1b[0m
    \x1b[96mContrib: \x1b[93m{stats.total_repo_contributions}\x1b[0m"""
    t.toggle_show_cursor(False)
    t.gen_text(details, 1, count=5, contin=True)

    t.gen_prompt(t.curr_row + 1)
    t.toggle_show_cursor(True)
    t.gen_typing_text(
        "\x1b[92m# \xe8\xbf\x99\xe4\xb8\xaa\xe4\xb8\x96\xe7\x95\x8c"
        "\xe4\xbc\x9a\xe5\xa5\xbd\xe5\x90\x97\x1b[0m",
        t.curr_row,
        contin=True,
    )
    t.gen_text("", t.curr_row, count=100, contin=True)

    t.gen_gif()


if __name__ == "__main__":
    main()
