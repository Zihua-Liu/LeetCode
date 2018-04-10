#include <iostream>
using namespace std;

bool check_each_location(int row, int col, char** board, int boardRowSize, int boardColSize){
	if(board[row][col] >= '1' && board[row][col] <= '9')
	{
		if(row == boardRowSize - 1 && col == boardColSize - 1)
			return true;

		if(col == boardColSize - 1)
			return check_each_location(row + 1, 0, board, boardRowSize, boardColSize);
		else
			return check_each_location(row, col + 1, board, boardRowSize, boardColSize);
	}	
	bool valid_num[10];
	for (int i = 1; i <= 9; i++)
		valid_num[i] = true;
	for (int i = 0; i < boardColSize; i++)
	{
		if (board[row][i] >= '1' && board[row][i] <= '9')
			valid_num[board[row][i] - '0'] = false;
	}
	for (int i = 0; i < boardRowSize; i++)
	{
		if (board[i][col] >= '1' && board[i][col] <= '9')
			valid_num[board[i][col] - '0'] = false;
	}
	int i_begin = row / 3;
	i_begin *= 3;
	int j_begin = col / 3;
	j_begin *= 3;
	for (int i = i_begin; i < i_begin + 3;i++)
	{
		for (int j = j_begin; j < j_begin + 3; j++)
		{
			if (board[i][j] >= '1' && board[i][j] <= '9')
				valid_num[board[i][j] - '0'] = false;
		}
	}
	bool result = false;
	for (int i = 1; i <= 9; i++)
	{
		if (valid_num[i] == true)
		{
			cout << "row: " << row << " col: " << col << endl;
			cout << "value" << i << endl;
			board[row][col] = i + '0';
			if(row == boardRowSize - 1 && col == boardColSize - 1)
				return true;
			if(col == boardColSize - 1)
				result = check_each_location(row + 1, 0, board, boardRowSize, boardColSize);
			else
				result = check_each_location(row, col + 1, board, boardRowSize, boardColSize);

			if (result)
				return true;
			else
				board[row][col] = '.';
		}
	}
	return result;
}

bool isValidSudoku(char** board, int boardRowSize, int boardColSize) {
    return check_each_location(0, 0, board, boardRowSize, boardColSize);
}

int main()
{
	char board[9][9];
	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			board[i][j] = '.';
			if (j == 0)
				board[i][j] = i + 1;
		}
	}
	board[0][0] = '.';
	for (int i = 1; i < 9; i++)
		board[0][i] = 9 - i;
	cout << isValidSudoku((char **)board, 9, 9);
}