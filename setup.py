from distutils.core import setup

setup(name='pycocoevalcap',
      version='1.0',
      packages=['pycocoevalcap', 'pycocoevalcap.tokenizer',
                'pycocoevalcap.rouge', 'pycocoevalcap.meteor',
                'pycocoevalcap.cider', 'pycocoevalcap.bleu'],
      package_dir={'pycocoevalcap': 'pycocoevalcap'}
      )
