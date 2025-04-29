from typing import Optional, TypedDict

import pulumi
import pulumi_random


class GreetingArgs(TypedDict):
    who: Optional[pulumi.Input[str]]
    """The entity we shall greet."""


class Greeting(pulumi.ComponentResource):
    message: pulumi.Output[Optional[str]]
    """The greeting message that has been ardouously generated."""

    def __init__(
        self,
        name: str,
        args: GreetingArgs,
        opts: Optional[pulumi.ResourceOptions] = None,
    ):
        super().__init__("greeter:index:Greeting", name, {}, opts)
        who = args.get("who") or "Pulumipus"

        greeting_word = pulumi_random.RandomShuffle(
            f"{name}-greeting",
            inputs=["Hello", "Bonjour", "Ciao", "Hola"],
            result_count=1,
            opts=pulumi.ResourceOptions(parent=self),
        )
        self.greeting = pulumi.Output.concat(greeting_word.results[0], ", ", who, "!")
        self.register_outputs({"greeting": self.greeting})
