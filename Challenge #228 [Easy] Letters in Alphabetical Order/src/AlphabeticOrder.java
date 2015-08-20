import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class AlphabeticOrder {
	private String str;
	private List<String> strAry;
	private String results;

	public AlphabeticOrder(String _str){
		str = _str;
		strAry = new ArrayList<String>(Arrays.asList(_str.split("(?!^)")));
		results = check();
	}
	
	public String getStr(){
		return str;
	}
	
	public String getResults(){
		return results;
	}
	
	public void printResults(){
		System.out.println(results);
	}
	
	private String check(){
		String strSorted = "";
		Collections.sort(strAry);
		
		for(int i = 0; i < strAry.size(); i++){
			strSorted += strAry.get(i).toString();
		}
		
		if(strSorted.equals(str)){
			return str + " IN ORDER";
		}
		
		return str + " NOT IN ORDER";
	}
}
