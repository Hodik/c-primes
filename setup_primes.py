import sys
import sysconfig

from setuptools import Extension, setup


def main():
    include_dirs = [sysconfig.get_path("include")]
    platinclude = sysconfig.get_path("platinclude")
    if platinclude != include_dirs[0]:
        include_dirs.append(platinclude)
    if sys.platform == "darwin":  # For Mac
        include_dirs.append(sysconfig.get_config_var("CONFINCLUDEPY"))

    setup(
        name="prime_c",
        version="1.0.0",
        description="Prime number generation in C",
        ext_modules=[
            Extension(
                "prime_c",
                ["primesmodule.c"],
                include_dirs=include_dirs,
                extra_link_args=["-lm"],
            )
        ],  # Link math library
    )


if __name__ == "__main__":
    main()
