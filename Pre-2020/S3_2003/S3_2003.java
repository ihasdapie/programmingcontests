//2002 s3 

import java.util.Scanner;
import java.util.Arrays;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collections;
public class S3_2003 {
		
	static Scanner input = new Scanner(System.in);
	static int numTiles = input.nextInt();
	static int numRows = input.nextInt();
	static int numColumns = input.nextInt();
	static int[][] floorPlan = new int[numRows][numColumns];
		
	
	public static void main(String[] args) {
		// create floor plan 


		for (int r = 0; r < numRows; r++) {
			String ln = input.next();
			for (int c = 0; c < numColumns; c++) {
				if (ln.charAt(c) == 'I'){
					floorPlan[r][c] = -1;
				}
				else{
					floorPlan[r][c] = 0;
				}
			}
		}
		
		//~ System.out.println(floorPlan[1][15]);

		
		
		//"I" is a wall, "." is floor space
		
		// find enclosed rooms
		// go through all "0"s. Check if all touching squares (break @ 1) are:
		//												1. of the same number
		//												2. if empty, assign number to that spot
		// make modifications directly onto the floorplan

		
		int currentRoom = 1;
		
		//last step will be to go thru the floorplan again and simply count up the instances of rooms from 0 -> n 
		// then arithmetic for output
		
		
		for (int r = 0; r < numRows; r++){
			for (int c = 0; c < numColumns; c++){
				if (floorPlan[r][c] == 0){
					fillRoom(r, c, floorPlan, currentRoom);
					currentRoom++;
				}
			}
		}
		
		//~ printPlan(numRows, numColumns, floorPlan);
	
		HashMap<Integer, Integer> rooms = new HashMap<Integer, Integer>();
		
		for (int i = 1; i < currentRoom; i++){
			rooms.put(i, 0);
		}
		
		//~ System.out.println(rooms);
		//~ System.out.println(currentRoom);
		//~ printPlan(numRows, numColumns, floorPlan);

		for (int r = 0; r < numRows; r++){
			for (int c = 0; c< numColumns; c++){
				int x = floorPlan[r][c];
				if (x != -1){
					rooms.put(x, (rooms.get(x)+1));
				}
			}
				
		}

		//~ System.out.println(rooms);
		
		ArrayList<Integer> roomSize = new ArrayList<Integer>();
		
		for (Integer i: rooms.values()){
			roomSize.add(i);
		}
		
		Collections.sort(roomSize, Collections.reverseOrder());
		
		//~ System.out.println(roomSize);
		
		
		int numRooms = 0;
		
		for (Integer i: roomSize){
			if (numTiles < i){
				break;
			}
			if ((numTiles-i) >= 0){
				numTiles = numTiles - i;
				numRooms++;
			
			
			}
		}
		
		if (numRooms == 1){
			System.out.println(numRooms+" room, "+numTiles+" square metre(s) left over");
		}
		else{
			System.out.println(numRooms+" rooms, "+numTiles+" square metre(s) left over");
		}
			
		
	
	
	}

	public static void fillRoom(int r, int c, int[][] floorPlan, int currentRoom){
		//recursively fills up rooms with a number
		int currentValue = floorPlan[r][c];
	
		//~ if (currentValue != currentRoom){
			//~ ;
		//~ }
		
		if (currentValue == 0){
			floorPlan[r][c] = currentRoom;
			if ((r+1 < numRows) && c< numColumns){
				fillRoom(r+1, c, floorPlan, currentRoom);
			}

			if ((r-1 > 0) && c< numColumns){
				fillRoom(r-1, c, floorPlan, currentRoom);
			}
			
			if ((r < numRows) && c+1 < numColumns){
				fillRoom(r, c+1, floorPlan, currentRoom);
			}

			if ((r < numRows) && c-1 >0 ){
				fillRoom(r, c-1, floorPlan, currentRoom);
			}
			
		}
	}
	
	
	public static void printPlan(int numRows, int numColumns, int[][] floorPlan){
			
	//print floorplan
		for (int r = 0; r < numRows; r++){
			String out = "";
			for (int c = 0; c < numColumns; c++){
				out = out + String.valueOf(floorPlan[r][c]);
			}
			System.out.println(out);
		}
	}

}
