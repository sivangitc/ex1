from typing import List, Any

UNCLEAN_MARK = '.'
CLEAN_MARK = 'X'

BOARD_SIZE = 5


class Coords:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    def right(self) -> Any:
        return Coords(self.row, self.col + 1)

    def left(self) -> Any:
        return Coords(self.row, self.col - 1)

    def up(self) -> Any:
        return Coords(self.row - 1, self.col)

    def down(self) -> Any:
        return Coords(self.row + 1, self.col)


class Board:
    def __init__(self, size: int) -> None:
        self.init_state(UNCLEAN_MARK, size)
        self.size = size
        self.pos = Coords(0, 0)
        self.mark = UNCLEAN_MARK

    def init_state(self, mark: str, size: int) -> None:
        self.state: List[List[str]] = []
        for _ in range(size):
            self.state.append([])
        for row in self.state:
            for _ in range(size):
                row.append(mark)

    def is_valid_coords(self, coords: Coords) -> bool:
        """Checks if given coords are within the board"""
        return coords.row >= 0 and coords.row < self.size and \
            coords.col >= 0 and coords.col < self.size

    def try_clean(self) -> None:
        if self.mark == CLEAN_MARK:
            self.state[self.pos.row][self.pos.col] = CLEAN_MARK

    def try_set_pos(self, coords: Coords) -> str:
        """Return: error string or '' if succeeded"""
        if not self.is_valid_coords(coords):
            return f"Invalid pos {coords}"
        self.pos = coords
        self.try_clean()
        return ""

    def try_move_direction(self, direction: str) -> str:
        """Return: error string or '' if succeeded"""
        if direction not in ["right", "left", "up", "down"]:
            return f"invalid direction {direction}"
        # for example, try set pos to self.pos.right()
        return self.try_set_pos(self.pos.__getattribute__(direction)())

    def set_on(self) -> None:
        self.mark = CLEAN_MARK

    def set_off(self) -> None:
        self.mark = UNCLEAN_MARK

    def print_board(self) -> None:
        for row in self.state:
            for mark in row:
                print(mark, end=' ')
            print()


class Robot:
    def __init__(self, board: Board):
        self.direction = ""
        self.board = board
        self.speed = 1

    def do_batch_instructions(self, instructions_line: str) -> None:
        instructions = instructions_line.split()
        for instr in instructions:
            output = self.do_instruction(instr)
            if output:
                print(output)

    def do_instruction(self, instr: str) -> str:
        """Return: error string or '' if succeeded"""
        if instr in ["right", "left", "up", "down"]:
            self.direction = instr
            return ""
        if instr.isnumeric():
            if not self.direction:
                return "no direction set"
            return self.move(int(instr))
        if instr == "on":
            self.board.set_on()
            return ""
        if instr == "off":
            self.board.set_off()
            return ""
        if instr == "turbo":
            self.speed = 2
            return ""
        if instr == "normal":
            self.speed = 1
            return ""
        return f"instruction {instr} not found"

    def move(self, count: int) -> str:
        """Return: error string or '' if succeeded"""
        for _ in range(count * self.speed):
            output = self.board.try_move_direction(self.direction)
            if output:
                return output
        return ""


def main() -> None:
    board = Board(BOARD_SIZE)
    robot = Robot(board)
    instructions = input("Instructions: ")
    # instructions = "right on 4 down 2 off 2 left on 2 up 2 off 2"
    # instructions = "right on turbo 2 down 1 normal off 2 left on 2 up 2 off 2"
    robot.do_batch_instructions(instructions)
    board.print_board()


if __name__ == "__main__":
    main()
