import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Sentence {
	private String sentence;
	private String manglingSentence;
	
	public Sentence(String inSentence) {
		sentence = inSentence;
		manglingSentence = setManglingSentence(sentence);
	}
	
	public String getSentence(){
		return sentence;
	}
	
	public String getManglingSentence(){
		return manglingSentence;
	}
	
	private String capitalize(String word) {
		return Character.toUpperCase(word.charAt(0)) + word.substring(1);
	}
	
	private String shuffle(String word) {
        String shuffledString = "";
        Boolean initCap = false;

        if(Character.isUpperCase(word.charAt(0))){
        	initCap = true;
        }
        
        word = word.toLowerCase();
        
        while (word.length() != 0)
        {
            int index = (int) Math.floor(Math.random() * word.length());
            char c = word.charAt(index);
            word = word.substring(0,index)+word.substring(index+1);
            shuffledString += c;
        }

        if(initCap == true){
        	return capitalize(shuffledString);
        }
        return shuffledString;
	}
	
	private String handleSpecialCharacters(String inStr){
		
		if(inStr.contains(",")) {
			return shuffle(inStr.substring(0, inStr.length()-1)) + ",";
		} else if(inStr.contains("'")){
			return handleApostrophe(inStr);
		}
			
		return shuffle(inStr);
	}
	
	private String handleApostrophe(String inStr){
		List<String> x = new ArrayList<String>(Arrays.asList(inStr.split("'")));
		return shuffle(x.get(0)) + "'" + shuffle(x.get(1)); 
	}
	
	private String setManglingSentence(String inSentence) {
		List<String> x = new ArrayList<String>(Arrays.asList(inSentence.split("\\s|\\.")));
		List<String> jumbledString = new ArrayList<String>(); 
		
		for(String i : x){
			jumbledString.add(handleSpecialCharacters(i));
		}
		
		String rtn = "";
		for(String q : jumbledString){
			rtn += q + " ";
		}

		return rtn.substring(0, rtn.length()-1) + ".";
	}
	
}
