import rich
from rich.table import Table
def judge_directions_on_maps():
    underlined1 = "[underline green]北[/underline green]"
    underlined2 = "[underline green]南[/underline green]"
    underlined3 = "[underline green]西[/underline green]"
    underlined4 = "[underline green]东[/underline green]"
    underlined5 = "[underline green]北方[/underline green]"
    underlined6 = "[underline green]东西[/underline green]"
    underlined7 = "[underline green]南北[/underline green]"
    normal = f"[green]一般地图：上{underlined1}下{underlined2}，左{underlined3}右{underlined4}[/green]"
    label = f"[green]有指向标的地图：指向标箭头的指向↗为{underlined5}[/green]"
    line = f"[green]经纬线的地图：纬线指示{underlined6}，经线指示{underlined7}[/green]"
    rich.print(normal)
    rich.print(label)
    rich.print(line)
def scale():
    rich.print("[bold red]       图上距离[/bold red]")
    rich.print("[bold red]比例尺=--------[/bold red]")
    rich.print("[bold red]       实地距离[/bold red]")
    table = Table()
    table.add_column("")
    table.add_column("比例尺")
    table.add_column("表示范围")
    table.add_column("表示内容")
    table.add_row("1:1000", "大", "小", "详细")
    table.add_row("1:100000", "小", "大", "粗略")
    rich.print(table)

#----------test cases---------#
scale()
