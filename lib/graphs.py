from process_data import raw_dataset

print(raw_dataset[:5])

raw_dataset.sort_values(by=['bookCount'], inplace=True, ascending=False)

book_count_plot_bar = raw_dataset[:5].filter(['bookCount']).plot.bar()

book_count_plot_pie = raw_dataset[:5].filter(
    ['bookCount']).plot.pie(subplots=True)[0]

raw_dataset.sort_values(by=['githubLanguage.repos'],
                        inplace=True, ascending=False)

book_count_plot = raw_dataset[:5].filter(['bookCount']).plot()

github_lang_plot_bar = raw_dataset[:5].filter(
    ['githubLanguage.repos']).plot.bar()

github_lang_plot_pie = raw_dataset[:5].filter(
    ['githubLanguage.repos']).plot.pie(subplots=True)[0]

book_count_plot_bar.figure.savefig("book_count_plot_bar.png")
book_count_plot_pie.figure.savefig("book_count_plot_pie.png")
book_count_plot.figure.savefig("book_count_plot.png")
github_lang_plot_bar.figure.savefig("github_lang_plot_bar.png")
github_lang_plot_pie.figure.savefig("github_lang_plot_pie.png")
