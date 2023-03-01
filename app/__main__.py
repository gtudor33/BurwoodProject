import sys
import click
import uvicorn


@click.command()
@click.option("--reload", is_flag=True)
def main(reload=False):
    kwargs = {"reload": reload}

    uvicorn.run(
        # "app_test:app",
        "app:app",
        loop="uvloop",
        host="0.0.0.0",
        port=8080,
        log_level="info",
        **kwargs,
    )


if __name__ == "__main__":
    sys.exit(main())
