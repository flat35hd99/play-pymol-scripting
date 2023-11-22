import pymol

def main():
    pymol.pymol_argv = ['pymol','-c']
    pymol.finish_launching()

    pymol.cmd.load("1VII.pdb")
    pymol.cmd.png("output.png", width=500, height=500, dpi=300)

if __name__ == '__main__':
    main()
