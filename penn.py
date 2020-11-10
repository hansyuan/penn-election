from matplotlib import pyplot

print("Pennsylvania")

BIDEN_INITIAL = 2805000
TRUMP_INITIAL = 3120000

REPORTING_INITIAL = .86

TOTAL_INITIAL = (BIDEN_INITIAL + TRUMP_INITIAL) / REPORTING_INITIAL

VERBOSE = True

reporting = [
    .88, .88, .88, .88, .89, .88, .88, .88, .89, .89, .89,
    .88, .88, .88, .88, .88, .88, .88, .88, .88, .88, .89,
    .89, .89, .90, .90, .90, .90, .90, .90, .94, .98, .98,
    .98, .98, .98, .98, .98, .98, .98, .98, .98, .98, .99,
    .99, .99
]

bidens = [
    2895441, 2924362, 2925483, 2926112, 2946881, 2987385, 2993438, 3006818, 3015721, 3019142, 3051565,
    3113911, 3120731, 3125766, 3127552, 3127743, 3134290, 3137658, 3142463, 3143750, 3157309, 3199756,
    3200489, 3209598, 3217079, 3219263, 3235017, 3243717, 3255710, 3258529, 3258529, 3302987, 3310574,
    3310778, 3311673, 3311780, 3311927, 3315158, 3315521, 3316645, 3319552, 3324096, 3324151, 3334633,
    3337069, 3355387
]
trumps = [
    3154969, 3163949, 3164810, 3165278, 3177086, 3188778, 3192980, 3199203, 3202481, 3203544, 3215983,
    3229011, 3232131, 3234380, 3236175, 3236368, 3236928, 3238682, 3240387, 3240998, 3247875, 3264017,
    3264209, 3267879, 3270295, 3270885, 3277202, 3280102, 3281842, 3282842, 3282842, 3293239, 3297096,
    3297454, 3298011, 3298107, 3298207, 3300413, 3300980, 3301601, 3302630, 3304471, 3304619, 3307459,
    3308192, 3314164
]

assert all([i <= 1.0 for i in reporting]), "Forgot a decimal?"
assert len(reporting) == len(bidens)
assert len(bidens) == len(trumps)
for i in range(1, len(bidens)):
    assert bidens[i] >= bidens[i - 1]
    assert trumps[i] >= trumps[i - 1]


print("=" * 60)
print()

biden_percentages = []
trump_percentages = []

ratios = []
new_ratios = []


totals = []
races = []


for i in range(len(reporting)):

    biden_diff = bidens[i] - BIDEN_INITIAL
    trump_diff = trumps[i] - TRUMP_INITIAL
    
    race = bidens[i] - trumps[i]
    races += [race]


    ratio = biden_diff / (biden_diff + trump_diff)
    ratio = round(ratio, 3)
    ratios += [ratio]

    # if SHORTERN_PRINTS:
    print(f'Iteration {i} reporting at {int(reporting[i] * 100)}%. \n'
          f'Biden\'s ratio: {round(ratio * 100, 3)}% of the new vote since the 86% reporting. '
          # f'Above threshold: {ratio > 0.66}.'
          )
    if VERBOSE:
        print()
    # print(f"Biden: {bidens[i]}. Trump: {trumps[i]}. Reporting: {reporting[i]}.")

    total = (bidens[i] + trumps[i]) / reporting[i]
    totals += [total]
    if VERBOSE:
        print(f'Total: {int(total)}. Needed: {int(total/2)}')

        print()

    biden_progress = bidens[i] / (total / 2)
    trump_progress = trumps[i] / (total / 2)

    biden_percentages += [biden_progress]
    trump_percentages += [trump_progress]

    if VERBOSE:
        print(f"Biden is at {round(biden_progress*100, 1)}% with {bidens[i]} of {int(total/2)}. ")
        print(f"Biden needs {int(total / 2) - bidens[i]}. ")
        print()
        print(f"Trump is at {round(trump_progress*100, 1)}% with {trumps[i]} of {int(total/2)}. ")
        print(f"Trump needs {int(total / 2) - trumps[i]}. ")

    biden_needs = int(total / 2) - bidens[i]
    trump_needs = int(total / 2) - trumps[i]
    remaining = (bidens[i] + trumps[i]) / reporting[i] * (1.0 - reporting[i])
    new_ratio_needed = round(biden_needs / remaining * 100, 1)
    new_ratios += [new_ratio_needed]


    if VERBOSE:
        print()
        print(f"Delta - total num of votes since 86% reporting: {int(total - TOTAL_INITIAL)}.")
        print(f"Remaining: {int(remaining)}.")
        print(f"New ratio needed: {new_ratio_needed}%. ")

    if VERBOSE:
        print()
    print("=" * 60)
    if VERBOSE:
        print()

if not VERBOSE:
    print(f"New ratio needed: {new_ratio_needed}%. ")









biden_percentages = [b * 100 for b in biden_percentages]
trump_percentages = [b * 100 for b in trump_percentages]

pyplot.figure(figsize=(6, 25), dpi=80)




plot_count = 7
col_count = 1
subplot_number = plot_count * 100 + col_count * 10 + 1

def get_subplot_number():
    global subplot_number
    ret = subplot_number
    subplot_number += 1
    return ret

pyplot.subplot(get_subplot_number())
pyplot.plot([i for i in range(len(biden_percentages))], biden_percentages, 'b-', label='Biden')
pyplot.plot([i for i in range(len(biden_percentages))], trump_percentages, 'r-', label='Trump')
pyplot.plot([i for i in range(len(biden_percentages))], [100 for _ in biden_percentages], 'k')
pyplot.legend()
pyplot.title("Biden and Trump's progress towards majority vote.")
# pyplot.xlabel("Numbers being recorded. Not linear!")
# pyplot.ylabel("Progress towards majority of state vote.")
pyplot.grid('both')





pyplot.subplot(get_subplot_number())
pyplot.plot([i for i in range(len(races))], races, 'k')
pyplot.plot([i for i in range(len(races))], races, 'k.', label="n=biden-trump")
pyplot.plot([i for i in range(len(races))], [0 for _ in range(len(races))], 'r.')
pyplot.title("Differences in vote count Biden - Trump")
# pyplot.ylabel("n = Biden - Trump")
pyplot.legend()
pyplot.grid()



pyplot.subplot(get_subplot_number())
ratios = [r * 100 for r in ratios]
pyplot.plot([i for i in range(len(new_ratios))], ratios, ".k")
pyplot.plot([i for i in range(len(new_ratios))], ratios, "-k", label="Biden's ratio since 86% reporting")
pyplot.plot([i for i in range(len(new_ratios))], [66 for _ in range(len(new_ratios))],
            'r-', label="Biden's required minimum ratio")

pyplot.title("Biden's ratio")
# pyplot.ylabel("Biden's ratio of the new vote since 86% reporting. ")
pyplot.legend()
pyplot.grid()


pyplot.subplot(get_subplot_number())
pyplot.plot([i for i in range(len(new_ratios))], new_ratios, ".k")
running_averages = [new_ratios[0], (new_ratios[0] + new_ratios[1]) / 2]
for i in range(2, len(new_ratios)):
    avg = (new_ratios[i] + new_ratios[i - 1] + new_ratios[i - 2]) / 3
    running_averages += [avg]
pyplot.plot([i for i in range(len(running_averages))], running_averages, 'b',
            label="Biden's required ratio after this point.")
pyplot.title("Biden's ratio needed for Penn.")
# pyplot.xlabel("Numbers being recorded. Not linear!")
# pyplot.ylabel("Ratio that Biden needs after this point")
pyplot.legend()
pyplot.grid('both')





pyplot.subplot(get_subplot_number())
ratio_diffs = []
for i in range(1, len(new_ratios)):
    ratio_diffs += [new_ratios[i] - new_ratios[i - 1]]
xs = [i + 1 for i in range(len(ratio_diffs))]
pyplot.plot(xs, ratio_diffs, ".b")

pyplot.plot([i for i in range(len(new_ratios))], [0 for _ in range(len(new_ratios))], 'k')

running_averages = [ratio_diffs[0], (ratio_diffs[0] + ratio_diffs[1]) / 2]
# for ratio in ratio_diffs[2:]:
#     avg = (ratio + running_averages[-1] + running_averages[-2]) / 3
for i in range(2, len(ratio_diffs)):
    avg = (ratio_diffs[i] + ratio_diffs[i - 1] + ratio_diffs[i - 2]) / 3
    running_averages += [avg]

pyplot.plot([i + 1 for i in range(len(running_averages))], running_averages, 'g',
            label='change in Biden\'s required ratio')

pyplot.title("Change in Biden's ratio.")
# pyplot.xlabel("Numbers being recorded. Not linear!")
# pyplot.ylabel("Change in ratio that Biden needs after this point.")
pyplot.legend()
pyplot.grid()



pyplot.subplot(get_subplot_number())
xs = [i for i in range(len(totals))]
ys = totals
pyplot.plot(xs, ys, ".b")

running_averages = [totals[0], (totals[0] + totals[1]) / 2]
# for ratio in totals[2:]:
#     avg = (ratio + running_averages[-1] + running_averages[-2]) / 3
for i in range(2, len(totals)):
    avg = (totals[i] + totals[i - 1] + totals[i - 2]) / 3
    running_averages += [avg]

pyplot.plot([i for i in range(len(running_averages))], running_averages, 'g',
            label="Deduced total number of votes as a func of total reporting.")


pyplot.title("Total num votes as we record them")
# pyplot.xlabel("Numbers being recorded. Not linear. ")
# pyplot.ylabel("Total number of votes")
pyplot.legend()
pyplot.grid()




pyplot.subplot(get_subplot_number())
xs = [i for i in range(len(reporting))]
ys = [int(r * 100) for r in reporting]

pyplot.plot(xs, ys, 'b-', label="Percentage of votes")
pyplot.plot(xs, [100 for _ in xs], 'r-', label="All votes counted at 100%")
pyplot.title("Votes reporting in from the AP")
# pyplot.ylabel("Percentage of votes reported in Penn")
pyplot.ylim(85, 101)
pyplot.grid()
pyplot.legend()








pyplot.show()
























































