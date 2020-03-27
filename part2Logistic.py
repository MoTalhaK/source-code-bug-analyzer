import sys
import pandas as pd
import docx
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

f = open('logistic.txt', 'w')
sys.stdout = f
f1_avg, p_avg, r_avg = 0, 0, 0
# warnings.filterwarnings("ignore")
precision_avg = 0
recall_avg = 0
f1_list = []  # list for f1-scores
p_list = []  # list for precision
r_list = []  # list for recall
avg_f1_all_list = []
avg_p_all_list = []
avg_r_all_list = []
curr = 0


def learn_dt(file_train, file_test, penalty, dual, tol,
             C, fit_intercept, intercept_scaling, class_weight,
             random_state, solver, max_iter,
             verbose, warm_start, n_jobs, l1_ratio):
    global f1_list, p_list, r_list

    f1_num = 0
    p_num = 0
    r_num = 0
    # load the training data as a matrix
    dataset = pd.read_csv(file_train, header=0)

    # separate the data from the target attributes
    train_data = dataset.drop('500_Buggy?', axis=1)

    # remove unnecessary features
    train_data = train_data.drop('change_id', axis=1)
    train_data = train_data.drop('412_full_path', axis=1)
    train_data = train_data.drop('411_commit_time', axis=1)

    # the lables of training data. `label` is the title of the  last column in your CSV files
    train_target = dataset.iloc[:, -1]

    # load the testing data
    dataset2 = pd.read_csv(file_test, header=0)

    # separate the data from the target attributes
    test_data = dataset2.drop('500_Buggy?', axis=1)

    # remove unnecessary features
    test_data = test_data.drop('change_id', axis=1)
    test_data = test_data.drop('412_full_path', axis=1)
    test_data = test_data.drop('411_commit_time', axis=1)

    # the lables of test data
    test_target = dataset2.iloc[:, -1]

    l_regression = LogisticRegression(penalty=penalty, dual=dual, tol=tol,
                                      C=C, fit_intercept=fit_intercept, intercept_scaling=intercept_scaling,
                                      class_weight=class_weight,
                                      random_state=random_state, solver=solver, max_iter=max_iter,
                                      verbose=verbose, warm_start=warm_start, n_jobs=n_jobs, l1_ratio=l1_ratio)

    test_pred = l_regression.fit(train_data, train_target).predict(test_data)
    f1_num = round(f1_score(test_target, test_pred, labels=[0, 1], average='weighted'), 2)
    # print(f1_num)
    p_num = round(precision_score(test_target, test_pred, labels=[0, 1], average='weighted'), 2)
    r_num = round(recall_score(test_target, test_pred, labels=[0, 1], average='weighted'), 2)
    f1_list.append(f1_num)
    p_list.append(p_num)
    r_list.append(r_num)


def param_test(c_val):
    global avg_f1_all_list, avg_p_all_list, avg_r_all_list
    avg_f1_all, avg_p_all, avg_r_all = 0, 0, 0
    global f1_avg, p_avg, r_avg
    global curr
    for i in range(0, 6):
        learn_dt("./data/jackrabbit/" + str(i) + "/train.csv", "./data/jackrabbit/" + str(i) + "/test.csv",
                 penalty='l2', dual=False, tol=0.0001, C=c_val, fit_intercept=True, intercept_scaling=1,
                 class_weight=None, random_state=30, solver='liblinear', max_iter=10000, verbose=0,
                 warm_start=False, n_jobs=None, l1_ratio=None)

    f1_avg = sum(f1_list) / len(f1_list)
    p_avg = sum(p_list) / len(p_list)
    r_avg = sum(r_list) / len(r_list)

    avg_f1_all = avg_f1_all + f1_avg
    avg_p_all = avg_p_all + p_avg
    avg_r_all = avg_r_all + r_avg

    f1_avg, p_avg, r_avg = 0, 0, 0
    f1_list.clear()
    p_list.clear()
    r_list.clear()

    # jdt
    for i in range(0, 6):
        learn_dt("./data/jdt/" + str(i) + "/train.csv", "./data/jdt/" + str(i) + "/test.csv",
                 penalty='l2', dual=False, tol=0.0001, C=c_val, fit_intercept=True, intercept_scaling=1,
                 class_weight=None, random_state=30, solver='liblinear', max_iter=10000, verbose=0,
                 warm_start=False, n_jobs=None, l1_ratio=None)

    f1_avg = sum(f1_list) / len(f1_list)
    p_avg = sum(p_list) / len(p_list)
    r_avg = sum(r_list) / len(r_list)

    avg_f1_all = avg_f1_all + f1_avg
    avg_p_all = avg_p_all + p_avg
    avg_r_all = avg_r_all + r_avg

    f1_avg, p_avg, r_avg = 0, 0, 0
    f1_list.clear()
    p_list.clear()
    r_list.clear()

    # lucene
    for i in range(0, 6):
        learn_dt("./data/lucene/" + str(i) + "/train.csv", "./data/lucene/" + str(i) + "/test.csv",
                 penalty='l2', dual=False, tol=0.0001, C=c_val, fit_intercept=True, intercept_scaling=1,
                 class_weight=None, random_state=30, solver='liblinear', max_iter=10000, verbose=0,
                 warm_start=False, n_jobs=None, l1_ratio=None)

    f1_avg = sum(f1_list) / len(f1_list)
    p_avg = sum(p_list) / len(p_list)
    r_avg = sum(r_list) / len(r_list)

    avg_f1_all = avg_f1_all + f1_avg
    avg_p_all = avg_p_all + p_avg
    avg_r_all = avg_r_all + r_avg

    f1_avg, p_avg, r_avg = 0, 0, 0
    f1_list.clear()
    p_list.clear()
    r_list.clear()

    # xorg
    for i in range(0, 6):
        learn_dt("./data/xorg/" + str(i) + "/train.csv", "./data/xorg/" + str(i) + "/test.csv",
                 penalty='l2', dual=False, tol=0.0001, C=c_val, fit_intercept=True, intercept_scaling=1,
                 class_weight=None, random_state=30, solver='liblinear', max_iter=10000, verbose=0,
                 warm_start=False, n_jobs=None, l1_ratio=None)

    f1_avg = sum(f1_list) / len(f1_list)
    p_avg = sum(p_list) / len(p_list)
    r_avg = sum(r_list) / len(r_list)

    avg_f1_all = avg_f1_all + f1_avg
    avg_p_all = avg_p_all + p_avg
    avg_r_all = avg_r_all + r_avg

    f1_avg, p_avg, r_avg = 0, 0, 0
    f1_list.clear()
    p_list.clear()
    r_list.clear()

    avg_f1_all = (avg_f1_all / 4)
    avg_p_all = (avg_p_all / 4)
    avg_r_all = (avg_r_all / 4)

    avg_f1_all_list.append(round(avg_f1_all, 2))
    avg_p_all_list.append(round(avg_p_all, 2))
    avg_r_all_list.append(round(avg_r_all, 2))


doc = docx.Document("test.docx")


def to_doc(d_frame):
    # global doc
    t = doc.add_table(d_frame.shape[0] + 1, d_frame.shape[1])

    for j in range(df.shape[-1]):
        t.cell(0, j).text = df.columns[j]

    # add the rest of the data frame
    for i in range(df.shape[0]):
        for j in range(df.shape[-1]):
            t.cell(i + 1, j).text = str(df.values[i, j])
    doc.save("test.docx")


n_val = [0.0001, 0.001, 0.01, 0.1, 1, 10, 50, 100, 500, 1000]
for n in n_val:
    param_test(n)

df = pd.DataFrame(list(zip(n_val, avg_p_all_list, avg_r_all_list, avg_f1_all_list)),
                  columns=["C", "Precision", "Recall", "F1-Score"])
to_doc(df)
print(df)
avg_f1_all_list.clear()
avg_p_all_list.clear()
avg_r_all_list.clear()
f.close()