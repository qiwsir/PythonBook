#coding:utf-8
'''
filename: judgescore.py
'''
class Score:
    def __init__(self, scores):
        self.scores = scores

    @classmethod
    def from_csv(cls, score_csv_str):
        scores = list(map(int, score_csv_str.split(',')))
        return cls(scores) if cls.validate(scores) else cls(False)


    @staticmethod
    def validate(scores):
        for g in scores:
            if g < 0 or g > 100:
                return False
        return True

if __name__ == '__main__':
    # Try out some valid scores
    class_scores_valid = Score.from_csv('90, 80, 85, 94, 70')
    print('Got scores:', class_scores_valid.scores)

    # Should fail with invalid scores
    class_scores_invalid = Score.from_csv('92, -15, 99, 101, 77, 65, 100')
    print(class_scores_invalid.scores)
