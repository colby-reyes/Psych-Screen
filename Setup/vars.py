from fndef import *

App.__init__()
header="Over the past 2 weeks, how often have you been bothered by...\n"

dispOpts = {
    0:"0 - Not at all",
    1:"1 - Several days",
    2:"2 - More than half the days",
    3:"3 - Nearly every day",
    "Q":"\n( Enter Q to quit )"
}

phq_prompts = [
    Questionnaire(header, "Little interest or pleasure in doing things", dispOpts),
    Questionnaire(header, "Feeling down, depressed, or hopeless", dispOpts),
    Questionnaire(header, "Trouble falling asleep or staying asleep, or sleeping too much", dispOpts),
    Questionnaire(header, "Feeling tired or having little energy", dispOpts),
    Questionnaire(header, "Poor appetite or overeating", dispOpts),
    Questionnaire(header, "Feeling bad about yourself; feeling that you are a failure or that you have let yourself or your family down", dispOpts),
    Questionnaire(header, "Trouble concentrating on things (such as reading the newspaper or watching TV", dispOpts),
    Questionnaire(header, "Moving or speaking so slowly that other people could have noticed. Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual", dispOpts),
    Questionnaire(header, "Thoughts that you would be better off dead, or of hurting yourself", dispOpts)
]


endOpts = {
    0:"0 - Not difficult at all",
    1:"1 - Somewhat difficult",
    2:"2 - Very difficult",
    3:"3 - Extremely difficult",
    "Q":"\n( Enter Q to quit )"
}

endQ = [Questionnaire(head="",prompts="If you checked off any problems, how difficult have these problems made it for you to do your work, take care of things at home, or get along with other people?",answers=endOpts)]


score_now = run_qstnr(phq_prompts)
fin = run_qstnr(endQ)
dif = endOpts[fin]

print("Your PHQ-9 score today is: {}\nYou rated your level of difficulty as: {}".format(score_now,dif[4:]))