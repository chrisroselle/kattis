import sys

class Score:
    def __init__(self, shots):
        self.value = 0
        self.shots = list(shots)
        # print('new Score: {}'.format(shots))
        for (value, multiplier) in shots:
            # print('value = {} add value {} multi {}'.format(self.value, value, multiplier))
            self.value = self.value + (value * multiplier)
        # print('new Score value = {} shots = {}'.format(self.value, self.shots))
    
    def output(self):
        for value, multiplier in self.shots:
            if (multiplier == 1):
                print("single {}".format(value))
            if (multiplier == 2):
                print("double {}".format(value))
            if (multiplier == 3):
                print("triple {}".format(value))

def update(target):
    # print('---------------------------------------')
    # print('update target = {}'.format(target))
    for score in scores:
        s = scores[score]
        # print('testing score {} value={} shots={}'.format(score, s.value, s.shots))
        if (len(s.shots) < 3):
            if (target - s.value) > 60:
                continue
            for multiplier in range(1,4):
                for value in range(1,21):
                    if (s.value + (value * multiplier)) == target:
                        # print('hit: value={} add v={} m={}'.format(s.value, value, multiplier))
                        new_shots = s.shots.copy()
                        new_shots.append((value, multiplier))
                        # print('new shots: {}'.format(new_shots))
                        result = Score(new_shots)
                        return True, result
        else:
            if (target - s.value) > 59:
                continue
            tried = []
            for original_value, original_multiplier in s.shots:
                if (original_value, original_multiplier) in tried:
                    continue
                tried.append((original_value, original_multiplier))
                for new_multiplier in range(original_multiplier, 4):
                    if (new_multiplier != original_multiplier):
                        for new_value in range(1, 21): 
                            if (s.value - (original_value * original_multiplier) + (new_value * new_multiplier)) == target:
                                new_shots = s.shots.copy()
                                new_shots.remove((original_value,original_multiplier))
                                new_shots.append((new_value, new_multiplier))
                                result = Score(new_shots)
                                return True, result
                    else:
                        for new_value in range(original_value + 1, 21):
                            if (s.value - (original_value * original_multiplier) + (new_value * new_multiplier)) == target:
                                new_shots = s.shots.copy()
                                new_shots.remove((original_value,original_multiplier))
                                new_shots.append((new_value, new_multiplier))
                                result = Score(new_shots)
                                return True, result
    return False, None

scores = {}
first_list = [(1,1)]
scores[1] = Score(first_list)

target_score = int(input())

for i in range(2, target_score + 1):
    # print('iteration i={}'.format(i))
    possible, result = update(i)
    if (possible):
        scores[i] = result
    # print('all scores:')
    # for score in scores:
        # s = scores[score]
        # print ('score[{}] value={} shots={}'.format(score, s.value, s.shots))
    

    
if (target_score in scores):
    scores[target_score].output()
else:
    print("impossible")

