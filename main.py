from random import choice, randint

consonants = [
    'm',      'n',            'ŋ',

    'p',      't', 'tʃ',      'k',
    'b',      'd', 'dʒ',      'g',

    'f', 'θ', 's',  'ʃ',           'h',
    'v', 'ð', 'z',  'ʒ',

              'l',  'r', 'j', 'w',
]

stops = [
    'p', 't', 'k',
    'b', 'd', 'g'
]

stops_voiceless = [
    'p', 't', 'k'
]

fricatives = [
    'f', 'θ', 's', 'ʃ',
    'v', 'ð', 'z', 'ʒ',
]

fricatives_voiceless = [
    'f', 'θ', 's', 'ʃ'
]

approximants = [
    'l', 'r', 'j', 'w'
]

approximants_but_not_j_because_fuck_j_apparently = [
    'l', 'r', 'w'
]

nasals = [
    'm', 'n', 'ŋ'
]

nasals_onset = [
    'm', 'n'
]

vowels = [ #Might be a bad idea, who knows
    "ɪ", "iː",           "ʊ", "uː",
    "ɛ", "eː",                "oʊ",
    "æ",       "ʌ", "ɑ", 

            "aɪ", "ɔɪ", "aʊ", "ju",
]

onsetBases = consonants[:]
onsetBases.remove("ŋ")

def get_a_nice_organ_like_your_lungs_you_have_nice_lungs_not_saying_that_you_should_date_me_or_anything_for_your_lungs_or_anyhthing_I_just_think_theyre_kinda_hot_and_I_suppose_youre_pretty_but_damn_do_your_lungs_Make_me_horny_fuck_yeah(plosive: str):
            if plosive=='b' or plosive=='p':
                return 'm'
            elif plosive=='g' or plosive=='k':
                return 'ŋ'
            elif plosive in fricatives:
                return choice(nasals)
            else:
                return 'n'



def create_onset():
    def single():
        return choice(onsetBases)
    
    def stop_approximant():
        return \
            choice(stops) +\
            choice(approximants_but_not_j_because_fuck_j_apparently)

    def whatever_the_third_option_is():
        ive_given_up_on_variable_names_sorry = fricatives_voiceless[:]
        ive_given_up_on_variable_names_sorry.append('v')
        return \
            choice(ive_given_up_on_variable_names_sorry) +\
            choice(approximants_but_not_j_because_fuck_j_apparently)
    
    def stuff_with_ss_in_front_of_them():
        monster_list = stops_voiceless + nasals_onset + fricatives_voiceless
        return 's' + choice(monster_list)
    
    def more_stuff_with_ss_in_front_of_them_except_theyre_longer_now_fucking_hell_why_did_i_decide_to_do_this_this_was_a_mistake_ffs():
        monster_list_part_two_electric_boogaloo = stops_voiceless + fricatives_voiceless
        return 's' + choice(monster_list_part_two_electric_boogaloo) + choice(approximants)
    
    i = randint(0, 5)
    if i == 0:
        return "";
    elif i==1:
        return single()
    elif i==2:
        return stop_approximant()
    elif i==3:
        return whatever_the_third_option_is()
    elif i==4:
        return stuff_with_ss_in_front_of_them()
    elif i==5:
        return more_stuff_with_ss_in_front_of_them_except_theyre_longer_now_fucking_hell_why_did_i_decide_to_do_this_this_was_a_mistake_ffs()
    else:
        return "How did you end up here what the fuck"

def create_nucleus():
    return choice(vowels) # + ['l', 'r'] + nasals_onset)

def create_coda(): #and here I thought the onset was painstaking
    def single_pringle():
        templist = consonants[:]
        templist.remove('h')
        templist.remove('w')
        templist.remove("j")
        return choice(templist)
    
    def lateral_or_rhotic_plus_thing():
        return \
            choice(["l", "r"]) + \
            choice(stops + ["dʒ", "tʃ"] + fricatives + nasals)
    
    def rhotic_plus_lateral():
        return "rl"
    
    def nasal_and_homoorganic_stop_or_fricative_aaaaaaaaa():
        variable_name = choice(stops)

        return get_a_nice_organ_like_your_lungs_you_have_nice_lungs_not_saying_that_you_should_date_me_or_anything_for_your_lungs_or_anyhthing_I_just_think_theyre_kinda_hot_and_I_suppose_youre_pretty_but_damn_do_your_lungs_Make_me_horny_fuck_yeah(variable_name) + variable_name
    
    def voiceless_fricative_and_voiceless_stop_this_thing_is_making_me_lose_faith_in_my_understanding_of_emotions_because_im_not_enjoying_this_so_why_do_I_keep_doing_this(): 
        return choice(['l', 'r', '']) + choice(fricatives_voiceless) + choice(stops_voiceless)
    
    def two_voiceless_fricatives():
        return choice(['l', 'r', '']) + choice(fricatives_voiceless) + choice(fricatives_voiceless)
    
    def two_voiceless_plosives():
        return choice(['l', 'r', '']) + choice(stops_voiceless) + choice(stops_voiceless)
    
    def stop_and_fricative(): #I think this could give some illegal stuff but oh well, I've stopped caring at this point
        return choice(['l', 'r', '']) + choice(stops_voiceless) + choice(fricatives_voiceless) #Except if it's /dz/ but I can't figure out how to implement that because I'm tired as fuck help
    
    def second_to_last_thing():
        stop1 = choice(stops)

        return \
            choice(get_a_nice_organ_like_your_lungs_you_have_nice_lungs_not_saying_that_you_should_date_me_or_anything_for_your_lungs_or_anyhthing_I_just_think_theyre_kinda_hot_and_I_suppose_youre_pretty_but_damn_do_your_lungs_Make_me_horny_fuck_yeah(stop1)) + \
            choice(stop1) + \
            choice(stops_voiceless + fricatives_voiceless)
    
    def last_thing():
        return choice(['kst', 'ksθ'])
    
    n = randint(1, 10)
    if n==1:
        return single_pringle()
    elif n==2:
        return lateral_or_rhotic_plus_thing()
    elif n==3:
        return rhotic_plus_lateral()
    elif n==4:
        return nasal_and_homoorganic_stop_or_fricative_aaaaaaaaa()
    elif n==5:
        return voiceless_fricative_and_voiceless_stop_this_thing_is_making_me_lose_faith_in_my_understanding_of_emotions_because_im_not_enjoying_this_so_why_do_I_keep_doing_this()
    elif n==6:
        return two_voiceless_fricatives()
    elif n==7:
        return two_voiceless_plosives()
    elif n==8:
        return stop_and_fricative()
    elif n==9:
        return second_to_last_thing()
    elif n==10:
        return last_thing()
    else:
        return "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"


    
        



print("/" + create_onset() + create_nucleus() + create_coda() + "/")