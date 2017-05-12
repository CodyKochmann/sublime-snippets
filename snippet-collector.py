from os import listdir, chdir
from os.path import join
from pprint import pprint

snippet_path = '/Users/cody/Library/Application Support/Sublime Text 3/Packages/User/'
chdir(snippet_path)

listing = (i for i in  listdir('./'))

snippet_paths = ( i for i in listing if i.endswith('.sublime-snippet'))

snippets = {
    k:lambda i=open(k):(i.read(),i.close())[0] for k in snippet_paths
}

#for path in snippets:
#    print '='*80
#    print path
#    print '-'*80
#    print snippets[path]
#    print '-'*80
#    print snippets[path]()

git_path = '/Users/cody/git/sublime-snippets/'
chdir(git_path)

for snippet_name in snippets:
    with open(snippet_name, 'w') as f:
        print 'writing {}'.format(snippet_name)
        f.write(snippets[snippet_name]())
