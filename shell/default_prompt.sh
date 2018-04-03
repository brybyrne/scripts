#export PS1='\[\h:\W \u \$ '

# Git branch in prompt.
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

parse_git_dirty() {
    st=$(git status 2>/dev/null | tail -n 1)
    if [[ $st == "" ]]; then
        echo ''
    elif [[ $st == "nothing to commit (working directory clean)" ]]; then
        echo ''
    elif [[ $st == 'nothing added to commit but untracked files present (use "git add" to track)' ]]; then
        echo '?'
    else
        echo '*'
    fi
}

# coloring the terminal comman line
SB_GREEN="\[\033[32m\]"
SB_BLUE="\[\033[34m\]"
SB_RED="\[\033[31m\]"
SB_NOCOLOR="\[\033[0m\]"
export PS1="\[\h:\W \u$SB_GREEN\$(parse_git_branch)$SB_RED\$(parse_git_dirty)$SB_NOCOLOR \$ "
