from pypi_simple import PyPISimple


def simple():
    package = input('\npackage to be checked ')

    try:
        with PyPISimple() as client:
            requests_page = client.get_project_page(package)

    except:
        print("\n SOMETHING WENT WRONG !!!!! \n\n",
              "CHECK INTERNET CONNECTION OR DON'T KNOW WHAT HAPPENED !!!\n")

    pkg = requests_page.packages[0]

    print(pkg)
    print(type(pkg))

    print('\n', pkg, '\n')

    print('\n' + pkg.filename + '\n')

    print('\n' + pkg.url + '\n')

    print('\n' + pkg.project + '\n')

    print('\n' + pkg.version + '\n')

    print('\n' + pkg.package_type + '\n')

    # print('\n'+pkg.get_digest()+'\n','ENDs HERE !!!!') #wasnt working


if __name__ == '__main__':
    simple()
