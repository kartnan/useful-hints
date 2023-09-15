import behave
import copy

def before_feature(context, feature):
    input_num = context.config.userdata.get('input_num', '')
    numbers = input_num.split(",")
    print(numbers)
    features = (s for s in feature.scenarios if type(s) == behave.model.ScenarioOutline and
                'dynamic' in s.tags)
    for s in features:
        for e in s.examples:
            orig = copy.deepcopy(e.table.rows[0])
            e.table.rows = []
            for num in numbers:
                num = int(num)
                n = copy.deepcopy(orig)
                # This relies on knowing that the table has two rows.
                n.cells = ['{}'.format(num), '{}'.format(num*num)]
                e.table.rows.append(n)
