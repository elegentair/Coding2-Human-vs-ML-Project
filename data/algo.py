#Human algo. code
import get_data
get_data.pd.set_option('display.max_columns', None)
get_data.pd.set_option('display.max_rows', None)
get_data.df = get_data.df.reset_index()
print(get_data.df.head(10))
results_dict = {}
for i in get_data.df.itertuples():
    #print(i.Index)
    #Check 1
    if i.word_freq_your >= 0 and i.word_freq_your <= 1:
        if i.word_freq_internet == 0:
            results_dict[f"{i.index} Check 1"] = "No"
        else:
            results_dict[f"{i.index} Check 1"] = "Yes"
    else:
        results_dict[f"{i.index} Check 1"] = "Yes"
    #Check 2
    # if i.word_freq_original >= 0 and i.word_freq_original <= 2:
    #     if i.word_freq_re >= 0 and i.word_freq_re <= 5:
    #         results_dict[f"{i.index} Check 2"] = "No"
    #     else:
    #         results_dict[f"{i.index} Check 2"] = "Yes"
    # elif i.word_freq_re == 0 or i.word_freq_original == 0:
    #     results_dict[f"{i.index} Check 2"] = "No"
    # else:
    #     results_dict[f"{i.index} Check 2"] = "Yes"

#first_five_items = list(results_dict.items())[:20]

#for key, value in first_five_items:
    #print(f"Key: {key}, Value: {value}")

