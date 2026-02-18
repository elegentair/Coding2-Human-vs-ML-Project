#Human algo. code
import get_data
get_data.pd.set_option('display.max_columns', None)
get_data.pd.set_option('display.max_rows', None)
get_data.df = get_data.df.reset_index()
#print(get_data.df.head(10))
results_dict = {}
for i in get_data.df.itertuples():
    #print(i.Index)
    #Check 1
    if i.word_freq_your >= 0 and i.word_freq_your <= 1:
        if i.word_freq_internet == 0:
            results_dict[i.index] = "No"
        else:
            results_dict[i.index] = "Yes"
    else:
        results_dict[i.index] = "Yes"
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

#Here, we are getting the number of emails flagged spam and not spam
num_spam = 0
num_clear = 0
num_act_spam = 0
num_act_clear = 0
for i in results_dict.values():
    if i == "Yes":
        num_spam += 1
    elif i == "No":
        num_clear += 1
print(f"Detected: Spam: {num_spam}, Clear: {num_clear}")

#Here, we are getting the number of actual spam and not spam emails
for i in get_data.df.itertuples():
    if i.Class == 1:
        num_act_spam += 1
    elif i.Class == 0:
        num_act_clear += 1
print(f"Actual: Spam: {num_act_spam}, Clear: {num_act_clear}")

#Here, we are getting the percent accuracy of the algorithm:
num_accurate = 0
num_spam_ident_correct = 0
num_clear_ident_correct = 0

for i in get_data.df.itertuples():
    if i.Class == 1:
        answer = "Yes"
    elif i.Class == 0:
        answer = "No"
    if answer == results_dict[i.index]:
        correct = True
        num_accurate += 1
        if i.Class == 1 and correct:
            num_spam_ident_correct += 1
        elif i.Class == 0 and correct:
            num_clear_ident_correct += 1
    else:
        correct = False
percent_right = (num_accurate / 4601) * 100
percent_spam_right = (num_spam_ident_correct / num_act_spam) * 100
percent_clear_right = (num_clear_ident_correct / num_act_clear) * 100

print(f"The algorithm classified {percent_right}% emails correctly!")
print(f"The algorithm caught {percent_spam_right}% of spam emails!")
print(f"The algorithm let in {percent_clear_right}% of non-spam emails!")

lb = int(input("Enter lower bound for range of emails to see predicited/act. values: "))
ub = int(input("Enter upper bound for range of emails to see predicited/act. values: "))


for i in get_data.df.itertuples():
    if i.index >= lb and i.index <= ub:
        if i.Class == 1:
            ans = "Yes"
        elif i.Class == 0:
            ans = "No"
        print(f"{i.index}: Predicted: {results_dict[i.index]}, Actual: {ans}")
