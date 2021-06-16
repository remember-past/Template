from sacred import Experiment
ex = Experiment(save_git_info=False)

@ex.main
def my_main():
    pass