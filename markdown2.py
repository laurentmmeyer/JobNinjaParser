import mistletoe

from JobNinjaRenderer import JobNinjaRenderer


def markdown(text, *args, **kwargs):
    return mistletoe.markdown(text, JobNinjaRenderer)
