{
    'dataset_loader_train': {
        '__factory__': 'palladium.dataset.Table',
        'path': '../step1/iris.data',
        'names': [
            'sepal length',
            'sepal width',
            'petal length',
            'petal width',
            'species',
        ],
        'target_column': 'species',
        'sep': ',',
        'nrows': 100,
    },

    'dataset_loader_test': {
        '__copy__': 'dataset_loader_train',
        'nrows': None,
        'skiprows': 100,
    },

    'model_persister': {
        '__factory__': 'palladium.persistence.Database',
        'url': 'sqlite:///iris-model.db',
    },

    # NEW ---------------------------------------------------------------------
    'model': {
        '__factory__': 'model.create_pipeline',
    },

    'scoring': 'accuracy',

    'grid_search': {
        'param_grid': {
            'net__lr': [0.5, 0.7, 0.9],

            # YOUR CODE HERE:
            #
            # In addition to the learning rate, we also want to find
            # the optimal number of epochs to train.  The parameter's
            # name is 'max_epochs'.  Try a number of different
            # settings for max_epochs and see if you can improve the
            # test score.

            'net__max_epochs': [50, 70],
        },
        'cv': 5,
        'verbose': 4,
        'n_jobs': 1,
    },
    # NEW ---------------------------------------------------------------------
}
