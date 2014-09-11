function Selectstate(){
// ON selection of category this function will work

removeAllOptions(document.formID.state);
addOption(document.formID.state, "", "", "");
//addOption(document.formID.rstate, "", "--Choose your state--", "");
addOption(document.formID.state,"Abia", "Abia");
addOption(document.formID.state,"Abuja", "Abuja");
addOption(document.formID.state,"Adamawa", "Adamawa");
addOption(document.formID.state,"Akwa Ibom", "Akwa Ibom");
addOption(document.formID.state,"Anambra", "Anambra");
addOption(document.formID.state,"Bauchi", "Bauchi");
addOption(document.formID.state,"Bayelsa", "Bayelsa");
addOption(document.formID.state,"Benue", "Benue");
addOption(document.formID.state,"Borno", "Borno");
addOption(document.formID.state,"Cross River", "Cross River");
addOption(document.formID.state,"Delta", "Delta");
addOption(document.formID.state,"Ebonyi", "Ebonyi");
addOption(document.formID.state,"Edo", "Edo");
addOption(document.formID.state,"Ekiti", "Ekiti");
addOption(document.formID.state,"Enugu", "Enugu");
addOption(document.formID.state,"Gombe", "Gombe");
addOption(document.formID.state,"Imo", "Imo");
addOption(document.formID.state,"Jigawa", "Jigawa");
addOption(document.formID.state,"Kaduna", "Kaduna");
addOption(document.formID.state,"Kano", "Kano");
addOption(document.formID.state,"Katsina", "Katsina");
addOption(document.formID.state,"Kebbi", "Kebbi");
addOption(document.formID.state,"Kogi", "Kogi");
addOption(document.formID.state,"Kwara", "Kwara");
addOption(document.formID.state,"Lagos", "Lagos");
addOption(document.formID.state,"Nasarawa", "Nasarawa");
addOption(document.formID.state,"Niger", "Niger");
addOption(document.formID.state,"Ogun", "Ogun");
addOption(document.formID.state,"Ondo", "Ondo");
addOption(document.formID.state,"Osun", "Osun");
addOption(document.formID.state,"Oyo", "Oyo");
addOption(document.formID.state,"Plateau", "Plateau");
addOption(document.formID.state,"Rivers", "Rivers");
addOption(document.formID.state,"Sokoto", "Sokoto");
addOption(document.formID.state,"Taraba", "Taraba");
addOption(document.formID.state,"Yobe", "Yobe");
addOption(document.formID.state,"Zamfara", "Zamfara");

}
//////////////////
function Selectlga(){
// ON selection of category this function will work
removeAllOptions(document.formID.lga);
addOption(document.formID.lga, "", "", "");

if(document.formID.state.value == 'Abia'){
addOption(document.formID.lga,"Aba North", "Aba North");
addOption(document.formID.lga,"Aba South", "Aba South");
addOption(document.formID.lga,"Arochukwu", "Arochukwu");
addOption(document.formID.lga,"Bende", "Bende");
addOption(document.formID.lga,"Ikwuano", "Ikwuano");
addOption(document.formID.lga,"Isiala Ngwa North", "Isiala Ngwa North");
addOption(document.formID.lga,"Isiala Ngwa South", "Isiala Ngwa South");
addOption(document.formID.lga,"Isuikwuato", "Isuikwuato");
addOption(document.formID.lga,"Obi Ngwa", "Obi Ngwa");
addOption(document.formID.lga,"Ohafia", "Ohafia");
addOption(document.formID.lga,"Osisioma Ngwa", "Osisioma Ngwa");
addOption(document.formID.lga,"Ugwunagbo", "Ugwunagbo");
addOption(document.formID.lga,"Ukwa East", "Ukwa East");
addOption(document.formID.lga,"Ukwa West", "Ukwa West");
}

if(document.formID.state.value == 'Abuja'){
addOption(document.formID.lga,"Abaji", "Abaji");
addOption(document.formID.lga,"Abuja Municipal", "Abuja Municipal");
addOption(document.formID.lga,"Bwari", "Bwari");
addOption(document.formID.lga,"Gwagwalada", "Gwagwalada");
addOption(document.formID.lga,"Kuje", "Kuje");
addOption(document.formID.lga,"Kwali", "Kwali");
}

if(document.formID.state.value == 'Adamawa'){
addOption(document.formID.lga,"Fufore","Fufore");
addOption(document.formID.lga,"Ganye","Ganye");
addOption(document.formID.lga,"Gombi","Gombi");
addOption(document.formID.lga,"Guyuk","Guyuk");
addOption(document.formID.lga,"Hong","Hong");
addOption(document.formID.lga,"Jada","Jada");
addOption(document.formID.lga,"Shelleng","Shelleng");
addOption(document.formID.lga,"Demsa","Demsa");
addOption(document.formID.lga,"Madagali","Madagali");
addOption(document.formID.lga,"Maiha","Maiha");
addOption(document.formID.lga,"Mayo-Belwa","Mayo-Belwa");
addOption(document.formID.lga,"Michika","Michika");
addOption(document.formID.lga,"Mubi North","Mubi North");
addOption(document.formID.lga,"Numan","Numan");
addOption(document.formID.lga,"Song","Song");
addOption(document.formID.lga,"Mubi South","Mubi South");
addOption(document.formID.lga,"Yola North(State capital)","Yola North(State capital)");
addOption(document.formID.lga,"Yola South","Yola South");
addOption(document.formID.lga,"Girei","Girei");
addOption(document.formID.lga,"Toungo","Toungo");
addOption(document.formID.lga,"Lamurde","Lamurde");
}

if(document.formID.state.value == 'Akwa Ibom'){
addOption(document.formID.lga,"Abak","Abak");
addOption(document.formID.lga,"Eastern Obolo","Eastern Obolo");
addOption(document.formID.lga,"Eket","Eket");
addOption(document.formID.lga,"Esit-Eket","Esit-Eket");
addOption(document.formID.lga,"Essien Udim","Essien Udim");
addOption(document.formID.lga,"Etim-Ekpo","Etim-Ekpo");
addOption(document.formID.lga,"Etinan","Etinan");
addOption(document.formID.lga,"Ibeno","Ibeno");
addOption(document.formID.lga,"Ibesikpo-Asutan","Ibesikpo-Asutan");
addOption(document.formID.lga,"Ibiono-Ibom","Ibiono-Ibom");
addOption(document.formID.lga,"Ika-Annang","Ika-Annang");
addOption(document.formID.lga,"Ikono","Ikono");
addOption(document.formID.lga,"Ikot Abasi","Ikot Abasi");
addOption(document.formID.lga,"Ikot Ekpene","Ikot Ekpene");
addOption(document.formID.lga,"Ini","Ini");
addOption(document.formID.lga,"Itu","Itu");
addOption(document.formID.lga,"Mbo","Mbo");
addOption(document.formID.lga,"Mkpat-Enin","Mkpat-Enin");
addOption(document.formID.lga,"Nsit-Atai","Nsit-Atai");
addOption(document.formID.lga,"Nsit-Ibom","Nsit-Ibom");
addOption(document.formID.lga,"Nsit-Ubium","Nsit-Ubium");
addOption(document.formID.lga,"Obot-Akara","Obot-Akara");
addOption(document.formID.lga,"Okobo","Okobo");
addOption(document.formID.lga,"Onna","Onna");
addOption(document.formID.lga,"Oron","Oron");
addOption(document.formID.lga,"Oruk Anam","Oruk Anam");
addOption(document.formID.lga,"Ukanafun","Ukanafun");
addOption(document.formID.lga,"Udung-Uko","Udung-Uko");
addOption(document.formID.lga,"Uruan","Uruan");
addOption(document.formID.lga,"Urue-Offong/Oruko","Urue-Offong/Oruko");
addOption(document.formID.lga,"Uyo","Uyo");
}

if(document.formID.state.value == 'Anambra'){
addOption(document.formID.lga,"Aguata","Aguata");
addOption(document.formID.lga,"Awka North","Awka North");
addOption(document.formID.lga,"Awka South","Awka South");
addOption(document.formID.lga,"Anambra East","Anambra East");
addOption(document.formID.lga,"Anambra West","Anambra West");
addOption(document.formID.lga,"Anaocha","Anaocha");
addOption(document.formID.lga,"Ayamelum","Ayamelum");
addOption(document.formID.lga,"Dunukofia","Dunukofia");
addOption(document.formID.lga,"Ekwusigo","Ekwusigo");
addOption(document.formID.lga,"Idemili North","Idemili North");
addOption(document.formID.lga,"Idemili South","Idemili South");
addOption(document.formID.lga,"Ihiala","Ihiala");
addOption(document.formID.lga,"Njikoka","Njikoka");
addOption(document.formID.lga,"Nnewi North","Nnewi North");
addOption(document.formID.lga,"Nnewi South","Nnewi South");
addOption(document.formID.lga,"Ogbaru","Ogbaru");
addOption(document.formID.lga,"Onitsha North","Onitsha North");
addOption(document.formID.lga,"Onitsha South","Onitsha South");
addOption(document.formID.lga,"Orumba North","Orumba North");
addOption(document.formID.lga,"Orumba South","Orumba South");
addOption(document.formID.lga,"Oyi","Oyi");
}

if(document.formID.state.value == 'Bauchi'){
addOption(document.formID.lga,"Alkaleri","Alkaleri");
addOption(document.formID.lga,"Bauchi","Bauchi");
addOption(document.formID.lga,"Bogoro","Bogoro");
addOption(document.formID.lga,"Damban","Damban");
addOption(document.formID.lga,"Darazo","Darazo");
addOption(document.formID.lga,"Dass","Dass");
addOption(document.formID.lga,"Gamawa","Gamawa");
addOption(document.formID.lga,"Ganjuwa","Ganjuwa");
addOption(document.formID.lga,"Giade","Giade");
addOption(document.formID.lga,"Itas/Gadau","Itas/Gadau");
addOption(document.formID.lga,"Jama'are","Jama'are");
addOption(document.formID.lga,"Katagum","Katagum");
addOption(document.formID.lga,"Kirfi","Kirfi");
addOption(document.formID.lga,"Misau","Misau");
addOption(document.formID.lga,"Ningi","Ningi");
addOption(document.formID.lga,"Shira","Shira");
addOption(document.formID.lga,"Tafawa Balewa","Tafawa Balewa");
addOption(document.formID.lga,"Toro","Toro");
addOption(document.formID.lga,"Warji","Warji");
addOption(document.formID.lga,"Zaki","Zaki");
}

if(document.formID.state.value == 'Bayelsa'){
addOption(document.formID.lga,"Brass, Nigeria","Brass, Nigeria");
addOption(document.formID.lga,"Ekeremor","Ekeremor");
addOption(document.formID.lga,"Kolokuma/Opokuma","Kolokuma/Opokuma");
addOption(document.formID.lga,"Nembe","Nembe");
addOption(document.formID.lga,"Ogbia","Ogbia");
addOption(document.formID.lga,"Sagbama","Sagbama");
addOption(document.formID.lga,"Southern Ijaw","Southern Ijaw");
addOption(document.formID.lga,"Yenagoa","Yenagoa");
}

if(document.formID.state.value == 'Benue'){
addOption(document.formID.lga,"Agatu","Agatu");
addOption(document.formID.lga,"Apa","Apa");
addOption(document.formID.lga,"Ado","Ado");
addOption(document.formID.lga,"Buruku","Buruku");
addOption(document.formID.lga,"Gboko","Gboko");
addOption(document.formID.lga,"Guma","Guma");
addOption(document.formID.lga,"Gwer East","Gwer East");
addOption(document.formID.lga,"Gwer West","Gwer West");
addOption(document.formID.lga,"Katsina-Ala","Katsina-Ala");
addOption(document.formID.lga,"Konshisha","Konshisha");
addOption(document.formID.lga,"Kwande","Kwande");
addOption(document.formID.lga,"Logo","Logo");
addOption(document.formID.lga,"Makurdi","Makurdi");
addOption(document.formID.lga,"Obi","Obi");
addOption(document.formID.lga,"Ogbadibo","Ogbadibo");
addOption(document.formID.lga,"Ohimini","Ohimini");
addOption(document.formID.lga,"Oju","Oju");
addOption(document.formID.lga,"Okpokwu","Okpokwu");
addOption(document.formID.lga,"Oturkpo","Oturkpo");
addOption(document.formID.lga,"Tarka","Tarka");
addOption(document.formID.lga,"Ukum","Ukum");
addOption(document.formID.lga,"Ushongo","Ushongo");
addOption(document.formID.lga,"Vandeikya","Vandeikya");
}

if(document.formID.state.value == 'Borno'){
addOption(document.formID.lga,"Abadam","Abadam");
addOption(document.formID.lga,"Askira/Uba","Askira/Uba");
addOption(document.formID.lga,"Bama","Bama");
addOption(document.formID.lga,"Bayo","Bayo");
addOption(document.formID.lga,"Biu","Biu");
addOption(document.formID.lga,"Chibok","Chibok");
addOption(document.formID.lga,"Damboa","Damboa");
addOption(document.formID.lga,"Dikwa","Dikwa");
addOption(document.formID.lga,"Gubio","Gubio");
addOption(document.formID.lga,"Guzamala","Guzamala");
addOption(document.formID.lga,"Gwange Sabon Lay","Gwange Sabon Lay");
addOption(document.formID.lga,"Gwoza","Gwoza");
addOption(document.formID.lga,"Hawul","Hawul");
addOption(document.formID.lga,"Jere","Jere");
addOption(document.formID.lga,"Kaga","Kaga");
addOption(document.formID.lga,"Kala/Balge","Kala/Balge");
addOption(document.formID.lga,"Konduga","Konduga");
addOption(document.formID.lga,"Kukawa","Kukawa");
addOption(document.formID.lga,"Kwaya Kusar","Kwaya Kusar");
addOption(document.formID.lga,"Mafa","Mafa");
addOption(document.formID.lga,"Magumeri","Magumeri");
addOption(document.formID.lga,"Maiduguri","Maiduguri");
addOption(document.formID.lga,"Marte","Marte");
addOption(document.formID.lga,"Mobbar","Mobbar");
addOption(document.formID.lga,"Monguno","Monguno");
addOption(document.formID.lga,"Ngala","Ngala");
addOption(document.formID.lga,"Nganzai","Nganzai");
addOption(document.formID.lga,"Shani","Shani");
}

if(document.formID.state.value == 'Cross River'){
addOption(document.formID.lga,"Abi","Abi");
addOption(document.formID.lga,"Akamkpa","Akamkpa");
addOption(document.formID.lga,"Akpabuyo","Akpabuyo");
addOption(document.formID.lga,"Bakassi","Bakassi");
addOption(document.formID.lga,"Bekwarra","Bekwarra");
addOption(document.formID.lga,"Biase","Biase");
addOption(document.formID.lga,"Boki","Boki");
addOption(document.formID.lga,"Calabar Municipal","Calabar Municipal");
addOption(document.formID.lga,"Calabar South","Calabar South");
addOption(document.formID.lga,"Etung","Etung");
addOption(document.formID.lga,"Ikom","Ikom");
addOption(document.formID.lga,"Obanliku","Obanliku");
addOption(document.formID.lga,"Obubra","Obubra");
addOption(document.formID.lga,"Obudu","Obudu");
addOption(document.formID.lga,"Odukpani","Odukpani");
addOption(document.formID.lga,"Ogoja","Ogoja");
addOption(document.formID.lga,"Yakuur","Yakuur");
addOption(document.formID.lga,"Yala","Yala");
}

if(document.formID.state.value == 'Delta'){
addOption(document.formID.lga,"Aniocha North","Aniocha North");
addOption(document.formID.lga,"Aniocha South","Aniocha South");
addOption(document.formID.lga,"Bomadi","Bomadi");
addOption(document.formID.lga,"Burutu","Burutu");
addOption(document.formID.lga,"Ethiope East","Ethiope East");
addOption(document.formID.lga,"Ethiope West","Ethiope West");
addOption(document.formID.lga,"Ika North East","Ika North East");
addOption(document.formID.lga,"Ika South","Ika South");
addOption(document.formID.lga,"Isoko North","Isoko North");
addOption(document.formID.lga,"Isoko South","Isoko South");
addOption(document.formID.lga,"Ndokwa East","Ndokwa East");
addOption(document.formID.lga,"Ndokwa West","Ndokwa West");
addOption(document.formID.lga,"Okpe","Okpe");
addOption(document.formID.lga,"Oshimili North","Oshimili North");
addOption(document.formID.lga,"Oshimili South","Oshimili South");
addOption(document.formID.lga,"Patani","Patani");
addOption(document.formID.lga,"Sapele","Sapele");
addOption(document.formID.lga,"Udu","Udu");
addOption(document.formID.lga,"Ughelli North","Ughelli North");
addOption(document.formID.lga,"Ughelli South","Ughelli South");
addOption(document.formID.lga,"Ukwuani","Ukwuani");
addOption(document.formID.lga,"Uvwie","Uvwie");
addOption(document.formID.lga,"Warri North","Warri North");
addOption(document.formID.lga,"Warri South","Warri South");
addOption(document.formID.lga,"Warri South West","Warri South West");
}

if(document.formID.state.value == 'Ebonyi'){
addOption(document.formID.lga,"Abakaliki","Abakaliki");
addOption(document.formID.lga,"Afikpo North","Afikpo North");
addOption(document.formID.lga,"Afikpo South","Afikpo South");
addOption(document.formID.lga,"Ebonyi","Ebonyi");
addOption(document.formID.lga,"Ezza North","Ezza North");
addOption(document.formID.lga,"Ezza South","Ezza South");
addOption(document.formID.lga,"Ikwo","Ikwo");
addOption(document.formID.lga,"Ishielu","Ishielu");
addOption(document.formID.lga,"Ivo","Ivo");
addOption(document.formID.lga,"Izzi","Izzi");
addOption(document.formID.lga,"Ohaozara","Ohaozara");
addOption(document.formID.lga,"Ohaukwu","Ohaukwu");
addOption(document.formID.lga,"Onicha","Onicha");
}

if(document.formID.state.value == 'Edo'){
addOption(document.formID.lga,"Akoko Edo","Akoko Edo");
addOption(document.formID.lga,"Egor","Egor");
addOption(document.formID.lga,"Esan North-East","Esan North-East");
addOption(document.formID.lga,"Esan Central","Esan Central");
addOption(document.formID.lga,"Esan South-East","Esan South-East");
addOption(document.formID.lga,"Esan West","Esan West");
addOption(document.formID.lga,"Etsako Central","Etsako Central");
addOption(document.formID.lga,"Etsako East","Etsako East");
addOption(document.formID.lga,"Etsako West","Etsako West");
addOption(document.formID.lga,"Igueben","Igueben");
addOption(document.formID.lga,"Ikpoba Okha","Ikpoba Okha");
addOption(document.formID.lga,"Oredo","Oredo");
addOption(document.formID.lga,"Orhionmwon","Orhionmwon");
addOption(document.formID.lga,"Ovia North-East","Ovia North-East");
addOption(document.formID.lga,"Ovia South-West","Ovia South-West");
addOption(document.formID.lga,"Owan East","Owan East");
addOption(document.formID.lga,"Owan West","Owan West");
addOption(document.formID.lga,"Uhunmwonde","Uhunmwonde");
}

if(document.formID.state.value == 'Ekiti'){
addOption(document.formID.lga,"Ado-Ekiti","Ado-Ekiti");
addOption(document.formID.lga,"Aiyekire (Gbonyin)","Aiyekire (Gbonyin)");
addOption(document.formID.lga,"Efon","Efon");
addOption(document.formID.lga,"Ekiti East","Ekiti East");
addOption(document.formID.lga,"Ekiti South-West","Ekiti South-West");
addOption(document.formID.lga,"Ekiti West","Ekiti West");
addOption(document.formID.lga,"Emure","Emure");
addOption(document.formID.lga,"Ido-Osi","Ido-Osi");
addOption(document.formID.lga,"Ijero","Ijero");
addOption(document.formID.lga,"Ikere","Ikere");
addOption(document.formID.lga,"Ikole","AIkole");
addOption(document.formID.lga,"Ilejemeje","Ilejemeje");
addOption(document.formID.lga,"Irepodun/Ifelodun","Irepodun/Ifelodun");
addOption(document.formID.lga,"Ise/Orun","Ise/Orun");
addOption(document.formID.lga,"Moba","Moba");
addOption(document.formID.lga,"Oye","Oye");
}

if(document.formID.state.value == 'Enugu'){
addOption(document.formID.lga,"Aninri","Aninri");
addOption(document.formID.lga,"Awgu","Awgu");
addOption(document.formID.lga,"Enugu East","Enugu East");
addOption(document.formID.lga,"Enugu North","Enugu North");
addOption(document.formID.lga,"Enugu South","Enugu South");
addOption(document.formID.lga,"Ezeagu","Ezeaguu");
addOption(document.formID.lga,"Igbo Etiti","Igbo Etiti");
addOption(document.formID.lga,"Igbo Eze North","Igbo Eze North");
addOption(document.formID.lga,"Igbo Eze South","Igbo Eze South");
addOption(document.formID.lga,"Isi Uzo","Isi Uzo");
addOption(document.formID.lga,"Nkanu East","Nkanu East");
addOption(document.formID.lga,"Nkanu West","Nkanu West");
addOption(document.formID.lga,"Nsukka","Nsukka");
addOption(document.formID.lga,"Oji River","Oji River");
addOption(document.formID.lga,"Udenu","Udenu");
addOption(document.formID.lga,"Udi","Udi");
addOption(document.formID.lga,"Uzo Uwani","Uzo Uwani");
}

if(document.formID.state.value == 'Gombe'){
addOption(document.formID.lga,"Akko, Nigeria","Akko, Nigeria");
addOption(document.formID.lga,"Balanga, Nigeria","Balanga, Nigeria");
addOption(document.formID.lga,"Billiri","Billiri");
addOption(document.formID.lga,"Dukku","Dukku");
addOption(document.formID.lga,"Funakaye","Funakaye");
addOption(document.formID.lga,"Gombe, Nigeria","Gombe, Nigeria");
addOption(document.formID.lga,"Kaltungo","Kaltungo");
addOption(document.formID.lga,"Kwami","Kwami");
addOption(document.formID.lga,"Nafada","Nafada");
addOption(document.formID.lga,"Shongom","Shongom");
addOption(document.formID.lga,"Yamaltu/Deba","Yamaltu/Deba");
}

if(document.formID.state.value == 'Imo'){
addOption(document.formID.lga,"Aboh Mbaise","Aboh Mbaise");
addOption(document.formID.lga,"Ahiazu Mbaise","Ahiazu Mbaise");
addOption(document.formID.lga,"Ehime Mbano","Ehime Mbano");
addOption(document.formID.lga,"Ezinihitte","Ezinihitte");
addOption(document.formID.lga,"Ideato North","Ideato North");
addOption(document.formID.lga,"Ideato South","Ideato South");
addOption(document.formID.lga,"Ihitte/Uboma","Ihitte/Uboma");
addOption(document.formID.lga,"Ikeduru","Ikeduru");
addOption(document.formID.lga,"Isiala Mbano","Isiala Mbano");
addOption(document.formID.lga,"Isu","Isu");
addOption(document.formID.lga,"Mbaitoli","Mbaitoli");
addOption(document.formID.lga,"Ngor Okpala","Ngor Okpala");
addOption(document.formID.lga,"Njaba","Njaba");
addOption(document.formID.lga,"Nkwerre","Nkwerre");
addOption(document.formID.lga,"Nwangele","Nwangele");
addOption(document.formID.lga,"Obowo","Obowo");
addOption(document.formID.lga,"Oguta","Oguta");
addOption(document.formID.lga,"Ohaji/Egbema","Ohaji/Egbema");
addOption(document.formID.lga,"Okigwe","Okigwe");
addOption(document.formID.lga,"Onuimo","Onuimo");
addOption(document.formID.lga,"Orlu","Orlu");
addOption(document.formID.lga,"Orsu","Orsu");
addOption(document.formID.lga,"Oru East","Oru East");
addOption(document.formID.lga,"Oru West","Oru West");
addOption(document.formID.lga,"Owerri Municipal","Owerri Municipal");
addOption(document.formID.lga,"Owerri North","Owerri North");
addOption(document.formID.lga,"Owerri West","Owerri West");
}

if(document.formID.state.value == 'Jigawa'){
addOption(document.formID.lga,"Auyo","Auyo");
addOption(document.formID.lga,"Babura","Babura");
addOption(document.formID.lga,"Biriniwa","Biriniwa");
addOption(document.formID.lga,"Birnin Kudu","Birnin Kudu");
addOption(document.formID.lga,"Buji","Buji");
addOption(document.formID.lga,"Dutse","Dutse");
addOption(document.formID.lga,"Gagarawa","Gagarawa");
addOption(document.formID.lga,"Garki","Garki");
addOption(document.formID.lga,"Gumel","Gumel");
addOption(document.formID.lga,"Guri","Guri");
addOption(document.formID.lga,"Gwaram","Gwaram");
addOption(document.formID.lga,"Gwiwa","Gwiwa");
addOption(document.formID.lga,"Hadejia","Hadejia");
addOption(document.formID.lga,"Jahun","Jahun");
addOption(document.formID.lga,"Kafin Hausa","Kafin Hausa");
addOption(document.formID.lga,"Kaugama","Kaugama");
addOption(document.formID.lga,"Kazaure","Kazaure");
addOption(document.formID.lga,"Kiri Kasama","Kiri Kasama");
addOption(document.formID.lga,"Kiyawa","Kiyawa");
addOption(document.formID.lga,"Maigatari","Maigatari");
addOption(document.formID.lga,"Malam Madori","Malam Madori");
addOption(document.formID.lga,"Miga","Miga");
addOption(document.formID.lga,"Ringim","Ringim");
addOption(document.formID.lga,"Roni","Roni");
addOption(document.formID.lga,"Sule Tankarkar","Sule Tankarkar");
addOption(document.formID.lga,"Taura","Taura");
addOption(document.formID.lga,"Yankwashi","Yankwashi");
}

if(document.formID.state.value == 'Kaduna'){
addOption(document.formID.lga,"Birnin Gwari","Birnin Gwari");
addOption(document.formID.lga,"Chikun","Chikun");
addOption(document.formID.lga,"Giwa","Giwa");
addOption(document.formID.lga,"Igabi","Igabi");
addOption(document.formID.lga,"Ikara","Ikara");
addOption(document.formID.lga,"Jaba","Jaba");
addOption(document.formID.lga,"Jema'a","Jema'a");
addOption(document.formID.lga,"Kachia","Kachia");
addOption(document.formID.lga,"Kaduna North","Kaduna North");
addOption(document.formID.lga,"Kaduna South","Kaduna South");
addOption(document.formID.lga,"Kagarko","Kagarko");
addOption(document.formID.lga,"Kajuru","Kajuru");
addOption(document.formID.lga,"Kaura","Kaura");
addOption(document.formID.lga,"Kauru","Kauru");
addOption(document.formID.lga,"Kubau","Kubau");
addOption(document.formID.lga,"Kudan","Kudan");
addOption(document.formID.lga,"Lere","Lere");
addOption(document.formID.lga,"Makarfi","Makarfi");
addOption(document.formID.lga,"Sabon Gari","Sabon Gari");
addOption(document.formID.lga,"Sanga","Sanga");
addOption(document.formID.lga,"Soba","Soba");
addOption(document.formID.lga,"Zangon Kataf","Zangon Kataf");
addOption(document.formID.lga,"Zaria","Zaria");
}

if(document.formID.state.value == 'Kano'){
addOption(document.formID.lga,"Ajingi","Ajingi");
addOption(document.formID.lga,"Albasu","Albasu");
addOption(document.formID.lga,"Bagwai","Bagwai");
addOption(document.formID.lga,"Bebeji","Bebeji");
addOption(document.formID.lga,"Bichi","Bichi");
addOption(document.formID.lga,"Bunkure","Bunkure");
addOption(document.formID.lga,"Dala","Dala");
addOption(document.formID.lga,"Dambatta","Dambatta");
addOption(document.formID.lga,"Dawakin Kudu","Dawakin Kudu");
addOption(document.formID.lga,"Dawakin Tofa","Dawakin Tofa");
addOption(document.formID.lga,"Doguwa","Doguwa");
addOption(document.formID.lga,"Fagge","Fagge");
addOption(document.formID.lga,"Gabasawa","Gabasawa");
addOption(document.formID.lga,"Garko","Garko");
addOption(document.formID.lga,"Garun Mallam","Garun Mallam");
addOption(document.formID.lga,"Gaya","Gaya");
addOption(document.formID.lga,"Gezawa","Gezawa");
addOption(document.formID.lga,"Gwale","Gwale");
addOption(document.formID.lga,"Gwarzo","Gwarzo");
addOption(document.formID.lga,"Kabo","Kabo");
addOption(document.formID.lga,"Kano Metropolitan Area","Kano Metropolitan Area");
addOption(document.formID.lga,"Kano Municipal","Kano Municipal");
addOption(document.formID.lga,"Karaye","Karaye");
addOption(document.formID.lga,"Kibiya","Kibiya");
addOption(document.formID.lga,"Kiru","Kiru");
addOption(document.formID.lga,"Kumbotso","Kumbotso");
addOption(document.formID.lga,"Kunchi","Kunchi");
addOption(document.formID.lga,"Kura","Kura");
addOption(document.formID.lga,"Madobi","Madobi");
addOption(document.formID.lga,"Makoda","Makoda");
addOption(document.formID.lga,"Minjibir","Minjibir");
addOption(document.formID.lga,"Nassarawa","Nassarawa");
addOption(document.formID.lga,"Rano","Rano");
addOption(document.formID.lga,"Rimin Gado","Rimin Gado");
addOption(document.formID.lga,"Rogo","Rogo");
addOption(document.formID.lga,"Shanono","Shanono");
addOption(document.formID.lga,"Sumaila","Sumaila");
addOption(document.formID.lga,"Takai","Takai");
addOption(document.formID.lga,"Tarauni","Tarauni");
addOption(document.formID.lga,"Tofa","Tofa");
addOption(document.formID.lga,"Tsanyawa","Tsanyawa");
addOption(document.formID.lga,"Tudun Wada","Tudun Wada");
addOption(document.formID.lga,"Ungogo","Ungogo");
addOption(document.formID.lga,"Warawa","Warawa");
addOption(document.formID.lga,"Wudil","Wudil");
}

if(document.formID.state.value == 'Katsina'){
addOption(document.formID.lga,"Bakori","Bakori");
addOption(document.formID.lga,"Batagarawa","Batagarawa");
addOption(document.formID.lga,"Batsari","Batsari");
addOption(document.formID.lga,"Baure","Baure");
addOption(document.formID.lga,"Charanchi","Charanchi");
addOption(document.formID.lga,"Dan Musa","Dan Musa");
addOption(document.formID.lga,"Dandume","Dandume");
addOption(document.formID.lga,"Danja","Danja");
addOption(document.formID.lga,"Daura","Daura");
addOption(document.formID.lga,"Dutsi","Dutsi");
addOption(document.formID.lga,"Dutsin-Ma","Dutsin-Ma");
addOption(document.formID.lga,"Faskari","Faskari");
addOption(document.formID.lga,"Funtua","Funtua");
addOption(document.formID.lga,"Ingawa","Ingawa");
addOption(document.formID.lga,"Jibia","Jibia");
addOption(document.formID.lga,"Kafur","Kafur");
addOption(document.formID.lga,"Kaita","Kaita");
addOption(document.formID.lga,"Kankara","Kankara");
addOption(document.formID.lga,"Katsina","Katsina");
addOption(document.formID.lga,"Kurfi","Kurfi");
addOption(document.formID.lga,"Kusada","Kusada");
addOption(document.formID.lga,"Mai'Adua","Mai'Adua");
addOption(document.formID.lga,"Malumfashi","Malumfashi");
addOption(document.formID.lga,"Mani","Mani");
addOption(document.formID.lga,"Mashi","Mashi");
addOption(document.formID.lga,"Matazu","Matazu");
addOption(document.formID.lga,"Musawa","Musawa");
addOption(document.formID.lga,"Rimi","Rimi");
addOption(document.formID.lga,"Sabuwa","Sabuwa");
addOption(document.formID.lga,"Safana","Safana");
addOption(document.formID.lga,"Sandamu","Sandamu");
addOption(document.formID.lga,"Zango","Zango");
}

if(document.formID.state.value == 'Kebbi'){
addOption(document.formID.lga,"Aleiro","Aleiro");
addOption(document.formID.lga,"Arewa Dandi","Arewa Dandi");
addOption(document.formID.lga,"Argungu","Argungu");
addOption(document.formID.lga,"Augie","Augie");
addOption(document.formID.lga,"Bagudo","Bagudo");
addOption(document.formID.lga,"Birnin Kebbi","Birnin Kebbi");
addOption(document.formID.lga,"Bunza","Bunza");
addOption(document.formID.lga,"Dandi","Dandi");
addOption(document.formID.lga,"Fakai","Fakai");
addOption(document.formID.lga,"Gwandu","Gwandu");
addOption(document.formID.lga,"Jega","Jega");
addOption(document.formID.lga,"Kalgo","Kalgo");
addOption(document.formID.lga,"Koko/Besse","Koko/Besse");
addOption(document.formID.lga,"Maiyama","Maiyama");
addOption(document.formID.lga,"Ngaski","Ngaski");
addOption(document.formID.lga,"Sakaba","Sakaba");
addOption(document.formID.lga,"Suru","Suru");
addOption(document.formID.lga,"Wasagu/Danko","Wasagu/Danko");
addOption(document.formID.lga,"Yauri","Yauri");
addOption(document.formID.lga,"Zuru","Zuru");
}

if(document.formID.state.value == 'Kogi'){
addOption(document.formID.lga,"Adavi","Adavi");
addOption(document.formID.lga,"Ajaokuta","Ajaokuta");
addOption(document.formID.lga,"Ankpa","Ankpa");
addOption(document.formID.lga,"Bassa","Bassa");
addOption(document.formID.lga,"Dekina","Dekina");
addOption(document.formID.lga,"Ibaji","Ibaji");
addOption(document.formID.lga,"Idah","Idah");
addOption(document.formID.lga,"Igalamela-Odolu","Igalamela-Odolu");
addOption(document.formID.lga,"Ijumu","Ijumu");
addOption(document.formID.lga,"Kabba/Bunu","Kabba/Bunu");
addOption(document.formID.lga,"Kogi","Kogi");
addOption(document.formID.lga,"Lokoja","Lokoja");
addOption(document.formID.lga,"Mopa-Muro","Mopa-Muro");
addOption(document.formID.lga,"Ofu","Ofu");
addOption(document.formID.lga,"Ogori/Magongo","Ogori/Magongo");
addOption(document.formID.lga,"Okehi","Okehi");
addOption(document.formID.lga,"Okene","Okene");
addOption(document.formID.lga,"Olamaboro","Olamaboro");
addOption(document.formID.lga,"Omala","Omala");
addOption(document.formID.lga,"Yagba East","Yagba East");
addOption(document.formID.lga,"Yagba West","Yagba West");
}

if(document.formID.state.value == 'Kwara'){
addOption(document.formID.lga,"Asa","Asa");
addOption(document.formID.lga,"Baruten","Baruten");
addOption(document.formID.lga,"Edu","Edu");
addOption(document.formID.lga,"Ifelodun","Ifelodun");
addOption(document.formID.lga,"Ilorin East","Ilorin East");
addOption(document.formID.lga,"Ilorin South","Ilorin South");
addOption(document.formID.lga,"Ilorin West","Ilorin West");
addOption(document.formID.lga,"Irepodun","Irepodun");
addOption(document.formID.lga,"Isin","Isin");
addOption(document.formID.lga,"Kaiama","Kaiama");
addOption(document.formID.lga,"Moro","Moro");
addOption(document.formID.lga,"Offa","Offa");
addOption(document.formID.lga,"Oke Ero","Oke Ero");
addOption(document.formID.lga,"Oyun","Oyun");
addOption(document.formID.lga,"Pategi","Pategi");
}

if(document.formID.state.value == 'Lagos'){
addOption(document.formID.lga,"Agege","Agege");
addOption(document.formID.lga,"Ajeromi-Ifelodun","Ajeromi-Ifelodun");
addOption(document.formID.lga,"Alimosho","Alimosho");
addOption(document.formID.lga,"Amuwo-Odofin","Amuwo-Odofin");
addOption(document.formID.lga,"Apapa","Apapa");
addOption(document.formID.lga,"Badagry","Badagry");
addOption(document.formID.lga,"Badagry Division","Badagry Division");
addOption(document.formID.lga,"Epe","Epe");
addOption(document.formID.lga,"Epe Division","Epe Division");
addOption(document.formID.lga,"Eti-Osa","Eti-Osa");
addOption(document.formID.lga,"Ibeju-Lekki","Ibeju-Lekki");
addOption(document.formID.lga,"Ifako-Ijaye","Ifako-Ijaye");
addOption(document.formID.lga,"Ikeja","Ikeja");
addOption(document.formID.lga,"Ikeja Division","Ikeja Division");
addOption(document.formID.lga,"Ikorodu","Ikorodu");
addOption(document.formID.lga,"Ikorodu Division","Ikorodu Division");
addOption(document.formID.lga,"Kosofe","Kosofe");
addOption(document.formID.lga,"Lagos Division","Lagos Division");
addOption(document.formID.lga,"Lagos Island","Lagos Island");
addOption(document.formID.lga,"Lagos Mainland","Lagos Mainland");
addOption(document.formID.lga,"Mushin","Mushin");
addOption(document.formID.lga,"Ojo","Ojo");
addOption(document.formID.lga,"Oshodi-Isolo","Oshodi-Isolo");
addOption(document.formID.lga,"Shomolu","Shomolu");
addOption(document.formID.lga,"Surulere","Surulere");
}

if(document.formID.state.value == 'Nasarawa'){
addOption(document.formID.lga,"Akwanga","Akwanga");
addOption(document.formID.lga,"Awe","Awe");
addOption(document.formID.lga,"Doma","Doma");
addOption(document.formID.lga,"Karu","Karu");
addOption(document.formID.lga,"Keana","Keana");
addOption(document.formID.lga,"Keffi","Keffi");
addOption(document.formID.lga,"Kokona","Kokona");
addOption(document.formID.lga,"Lafia","Lafia");
addOption(document.formID.lga,"Nasarawa","Nasarawa");
addOption(document.formID.lga,"Nasarawa Egon","Nasarawa Egon");
addOption(document.formID.lga,"Obi","Obi");
addOption(document.formID.lga,"Toto","Toto");
addOption(document.formID.lga,"Wamba","Wamba");
}

if(document.formID.state.value == 'Niger'){
addOption(document.formID.lga,"Agaie","Agaie");
addOption(document.formID.lga,"Agwara","Agwara");
addOption(document.formID.lga,"Bida","Bida");
addOption(document.formID.lga,"Borgu","Borgu");
addOption(document.formID.lga,"Bosso","Bosso");
addOption(document.formID.lga,"Chanchaga","Chanchaga");
addOption(document.formID.lga,"Edati","Edati");
addOption(document.formID.lga,"Gbako","Gbako");
addOption(document.formID.lga,"Gurara","Gurara");
addOption(document.formID.lga,"Katcha","Katcha");
addOption(document.formID.lga,"Kontagora","Kontagora");
addOption(document.formID.lga,"Lapai","Lapai");
addOption(document.formID.lga,"Lavun","Lavun");
addOption(document.formID.lga,"Magama","Magama");
addOption(document.formID.lga,"Mariga","Mariga");
addOption(document.formID.lga,"Mashegu","Mashegu");
addOption(document.formID.lga,"Mokwa","Mokwa");
addOption(document.formID.lga,"Munya","Munya");
addOption(document.formID.lga,"Paikoro","Paikoro");
addOption(document.formID.lga,"Rafi","Rafi");
addOption(document.formID.lga,"Rijau","Rijau");
addOption(document.formID.lga,"Shiroro","Shiroro");
addOption(document.formID.lga,"Suleja","Suleja");
addOption(document.formID.lga,"Tafa","Tafa");
addOption(document.formID.lga,"Wushishi","Wushishi");
}

if(document.formID.state.value == 'Ogun'){
addOption(document.formID.lga,"Abeokuta North","Abeokuta North");
addOption(document.formID.lga,"Abeokuta South","Abeokuta South");
addOption(document.formID.lga,"Ado-Odo/Ota","Ado-Odo/Ota");
addOption(document.formID.lga,"Ewekoro","Ewekoro");
addOption(document.formID.lga,"Ifo","Ifo");
addOption(document.formID.lga,"Ijebu East","Ijebu East");
addOption(document.formID.lga,"Ijebu North","Ijebu North");
addOption(document.formID.lga,"Ijebu North East","Ijebu North East");
addOption(document.formID.lga,"Ijebu Ode","Ijebu Ode");
addOption(document.formID.lga,"Ikenne","Ikenne");
addOption(document.formID.lga,"Imeko Afon","Imeko Afon");
addOption(document.formID.lga,"Ipokia","Ipokia");
addOption(document.formID.lga,"Obafemi Owode","Obafemi Owode");
addOption(document.formID.lga,"Odogbolu","Odogbolu");
addOption(document.formID.lga,"Odeda","Odeda");
addOption(document.formID.lga,"Ogun Waterside","Ogun Waterside");
addOption(document.formID.lga,"Remo North","Remo North");
addOption(document.formID.lga,"Sagamu or Shagamu","Sagamu or Shagamu");
addOption(document.formID.lga,"Yewa North formerly Egbado North","Yewa North formerly Egbado North");
addOption(document.formID.lga,"Yewa South formerly Egbado South","Yewa South formerly Egbado South");
}

if(document.formID.state.value == 'Ondo'){
addOption(document.formID.lga,"Akoko North-East headquarters in Ikare","Akoko North-East headquarters in Ikare");
addOption(document.formID.lga,"Akoko North-West","Akoko North-West");
addOption(document.formID.lga,"Akoko South-East","Akoko South-East");
addOption(document.formID.lga,"Akoko South-West","Akoko South-West");
addOption(document.formID.lga,"Akure North","Akure North");
addOption(document.formID.lga,"Akure South","Akure South");
addOption(document.formID.lga,"Ese Odo","Ese Odo");
addOption(document.formID.lga,"Idanre","Idanre");
addOption(document.formID.lga,"Ifedore","Ifedore");
addOption(document.formID.lga,"Ilaje","Ilaje");
addOption(document.formID.lga,"Ile Oluji/Okeigbo[2]","Ile Oluji/Okeigbo[2]");
addOption(document.formID.lga,"Irele","Irele");
addOption(document.formID.lga,"Odigbo","Odigbo");
addOption(document.formID.lga,"Okitipupa","Okitipupa");
addOption(document.formID.lga,"Ondo East","Ondo East");
addOption(document.formID.lga,"Ondo West","Ondo West");
addOption(document.formID.lga,"Ose","Ose");
addOption(document.formID.lga,"Owo","Owo");
}

if(document.formID.state.value == 'Osun'){
addOption(document.formID.lga,"Aiyedaade (Gbongan)","Aiyedaade (Gbongan)");
addOption(document.formID.lga,"Aiyedire (Ile Ogbo)","Aiyedire (Ile Ogbo)");
addOption(document.formID.lga,"Atakunmosa East (Iperindo)","Atakunmosa East (Iperindo)");
addOption(document.formID.lga,"Atakunmosa West (Osu)","Atakunmosa West (Osu)");
addOption(document.formID.lga,"Boluwaduro (Otan-Ayegbaju)","Boluwaduro (Otan-Ayegbaju)");
addOption(document.formID.lga,"Boripe (Iragbiji)","Boripe (Iragbiji)");
addOption(document.formID.lga,"Ede North (Oja Timi)","Ede North (Oja Timi)");
addOption(document.formID.lga,"Ede South (Ede)","Ede South (Ede)");
addOption(document.formID.lga,"Egbedore (Awo)","Egbedore (Awo)");
addOption(document.formID.lga,"Ejigbo (Ejigbo)","Ejigbo (Ejigbo)");
addOption(document.formID.lga,"Ife Central (Ile-Ife)","Ife Central (Ile-Ife)");
addOption(document.formID.lga,"Ife East (Oke-Ogbo)","Ife East (Oke-Ogbo)");
addOption(document.formID.lga,"Ife North (Ipetumodu)","Ife North (Ipetumodu)");
addOption(document.formID.lga,"Ife South (Ifetedo)","Ife South (Ifetedo)");
addOption(document.formID.lga,"Ifedayo (Oke-Ila Orangun)","Ifedayo (Oke-Ila Orangun)");
addOption(document.formID.lga,"Ifelodun (Ikirun)","Ifelodun (Ikirun)");
addOption(document.formID.lga,"Ila (Ila Orangun)","Ila (Ila Orangun)");
addOption(document.formID.lga,"Ilesa East (Ilesa)","Ilesa East (Ilesa)");
addOption(document.formID.lga,"Ilesa West (Ereja Square)","Ilesa West (Ereja Square)");
addOption(document.formID.lga,"Irepodun (Ilobu)","Irepodun (Ilobu)");
addOption(document.formID.lga,"Irewole (Ikire)","Irewole (Ikire)");
addOption(document.formID.lga,"Isokan (Apomu)","Isokan (Apomu)");
addOption(document.formID.lga,"Iwo (Iwo)","Iwo (Iwo)");
addOption(document.formID.lga,"Obokun (Ibokun)","Obokun (Ibokun)");
addOption(document.formID.lga,"Odo Otin (Okuku)","Odo Otin (Okuku)");
addOption(document.formID.lga,"Ola Oluwa (Bode Osi)","Ola Oluwa (Bode Osi)");
addOption(document.formID.lga,"Olorunda (Igbonna, Osogbo)","Olorunda (Igbonna, Osogbo)");
addOption(document.formID.lga,"Oriade (Ijebu-Jesa)","Oriade (Ijebu-Jesa)");
addOption(document.formID.lga,"Orolu (Ifon-Osun)","Orolu (Ifon-Osun)");
addOption(document.formID.lga,"Osogbo (Osogbo)","Osogbo (Osogbo)");
}

if(document.formID.state.value == 'Oyo'){
addOption(document.formID.lga,"Akinyele","Akinyele");
addOption(document.formID.lga,"Afijio","Afijio");
addOption(document.formID.lga,"Egbeda","Egbeda");
addOption(document.formID.lga,"Ibadan North","Ibadan North");
addOption(document.formID.lga,"Ibadan North-East","Ibadan North-East");
addOption(document.formID.lga,"Ibadan North-West","Ibadan North-West");
addOption(document.formID.lga,"Ibadan South-West","Ibadan South-West");
addOption(document.formID.lga,"Ibadan South-East","Ibadan South-East");
addOption(document.formID.lga,"Ibarapa Central","Ibarapa Central");
addOption(document.formID.lga,"Ibarapa East","Ibarapa East");
addOption(document.formID.lga,"Ido","Ido");
addOption(document.formID.lga,"Irepo","Irepo");
addOption(document.formID.lga,"Iseyin","Iseyin");
addOption(document.formID.lga,"Kajola","Kajola");
addOption(document.formID.lga,"Lagelu","Lagelu");
addOption(document.formID.lga,"Ogbomosho North","Ogbomosho North");
addOption(document.formID.lga,"Ogbomosho South","Ogbomosho South");
addOption(document.formID.lga,"Oyo West","Oyo West");
addOption(document.formID.lga,"Atiba","Atiba");
addOption(document.formID.lga,"Atigbo","Atigbo");
addOption(document.formID.lga,"Saki West","Saki West");
addOption(document.formID.lga,"Saki East","Saki East");
addOption(document.formID.lga,"Itesiwaju","Itesiwaju");
addOption(document.formID.lga,"Iwajowa","Iwajowa");
addOption(document.formID.lga,"Ibarapa North","Ibarapa North");
addOption(document.formID.lga,"Olorunsogo","Olorunsogo");
addOption(document.formID.lga,"Oluyole","Oluyole");
addOption(document.formID.lga,"Ogo Oluwa","Ogo Oluwa");
addOption(document.formID.lga,"Surulere","Surulere");
addOption(document.formID.lga,"Orelope","Orelope");
addOption(document.formID.lga,"Ori Ire","Ori Ire");
addOption(document.formID.lga,"Oyo East","Oyo East");
addOption(document.formID.lga,"Ona Ara","Ona Ara");
}

if(document.formID.state.value == 'Plateau'){
addOption(document.formID.lga,"Barkin Ladi","Barkin Ladi");
addOption(document.formID.lga,"Bassa","Bassa");
addOption(document.formID.lga,"Bokkos","Bokkos");
addOption(document.formID.lga,"Jos East","Jos East");
addOption(document.formID.lga,"Jos North","Jos North");
addOption(document.formID.lga,"Jos South","Jos South");
addOption(document.formID.lga,"Kanam","Kanam");
addOption(document.formID.lga,"Kanke","Kanke");
addOption(document.formID.lga,"Langtang North","Langtang North");
addOption(document.formID.lga,"Langtang South","Langtang South");
addOption(document.formID.lga,"Mangu","Mangu");
addOption(document.formID.lga,"Mikang","Mikang");
addOption(document.formID.lga,"Pankshin","Pankshin");
addOption(document.formID.lga,"Qua'an Pan","Qua'an Pan");
addOption(document.formID.lga,"Riyom","Riyom");
addOption(document.formID.lga,"Shendam","Shendam");
addOption(document.formID.lga,"Wase","Wase");
}

if(document.formID.state.value == 'Rivers'){
addOption(document.formID.lga,"Abua/Odual","Abua/Odual");
addOption(document.formID.lga,"Ahoada East","Ahoada East");
addOption(document.formID.lga,"Ahoada West","Ahoada West");
addOption(document.formID.lga,"Akuku-Toru","Akuku-Toru");
addOption(document.formID.lga,"Andoni","Andoni");
addOption(document.formID.lga,"Asari-Toru","Asari-Toru");
addOption(document.formID.lga,"Bonny","Bonny");
addOption(document.formID.lga,"Degema","Degema");
addOption(document.formID.lga,"Eleme","Eleme");
addOption(document.formID.lga,"Emohua","Emohua");
addOption(document.formID.lga,"Etche","Etche");
addOption(document.formID.lga,"Gokana","Gokana");
addOption(document.formID.lga,"Ikwerre","Ikwerre");
addOption(document.formID.lga,"Khana","Khana");
addOption(document.formID.lga,"Obio-Akpor","Obio-Akpor");
addOption(document.formID.lga,"Ogba/Egbema/Ndoni","Ogba/Egbema/Ndoni");
addOption(document.formID.lga,"Ogu/Bolo","Ogu/Bolo");
addOption(document.formID.lga,"Okrika","Okrika");
addOption(document.formID.lga,"Omuma","Omuma");
addOption(document.formID.lga,"Opobo/Nkoro","Opobo/Nkoro");
addOption(document.formID.lga,"Oyigbo","Oyigbo");
addOption(document.formID.lga,"Port Harcourt","Port Harcourt");
addOption(document.formID.lga,"Tai","Tai");
}

if(document.formID.state.value == 'Sokoto'){
addOption(document.formID.lga,"Binji","Binji");
addOption(document.formID.lga,"Bodinga","Bodinga");
addOption(document.formID.lga,"Dange Shuni","Dange Shuni");
addOption(document.formID.lga,"Gada","Gada");
addOption(document.formID.lga,"Goronyo","Goronyo");
addOption(document.formID.lga,"Gudu","Gudu");
addOption(document.formID.lga,"Gwadabawa","Gwadabawa");
addOption(document.formID.lga,"Illela","Illela");
addOption(document.formID.lga,"Isa","Isa");
addOption(document.formID.lga,"Kebbe","Kebbe");
addOption(document.formID.lga,"Kware","Kware");
addOption(document.formID.lga,"Rabah","Rabah");
addOption(document.formID.lga,"Sabon Birni","Sabon Birni");
addOption(document.formID.lga,"Shagari","Shagari");
addOption(document.formID.lga,"Silame","Silame");
addOption(document.formID.lga,"Sokoto North","Sokoto North");
addOption(document.formID.lga,"Sokoto South","Sokoto South");
addOption(document.formID.lga,"Tambuwal","Tambuwal");
addOption(document.formID.lga,"Tangaza","Tangaza");
addOption(document.formID.lga,"Tureta","Tureta");
addOption(document.formID.lga,"Wamako","Wamako");
addOption(document.formID.lga,"Wurno","Wurno");
addOption(document.formID.lga,"Yabo","Yabo");
}

if(document.formID.state.value == 'Taraba'){
addOption(document.formID.lga,"Ardo Kola","Ardo Kola");
addOption(document.formID.lga,"Bali, Nigeria","Bali, Nigeria")
addOption(document.formID.lga,"Donga, Nigeria","Donga, Nigeria")
addOption(document.formID.lga,"Gashaka","Gashaka")
addOption(document.formID.lga,"Gassol","Gassol")
addOption(document.formID.lga,"Ibi, Nigeria","Ibi, Nigeria")
addOption(document.formID.lga,"Jalingo","Jalingo")
addOption(document.formID.lga,"Karim Lamido","Karim Lamido")
addOption(document.formID.lga,"Kurmi, Nigeria","Kurmi, Nigeria")
addOption(document.formID.lga,"Lau, Nigeria","Lau, Nigeria")
addOption(document.formID.lga,"Sardauna, Nigeria","Sardauna, Nigeria")
addOption(document.formID.lga,"Takum","Takum")
addOption(document.formID.lga,"Ussa","Ussa")
addOption(document.formID.lga,"Wukari","Wukari")
addOption(document.formID.lga,"Yorro","Yorro")
addOption(document.formID.lga,"Zing, Nigeria","Zing, Nigeria")
}

if(document.formID.state.value == 'Yobe'){
addOption(document.formID.lga,"Bursari","Bursari");
addOption(document.formID.lga,"Damaturu","Damaturu")
addOption(document.formID.lga,"Geidam","Geidam")
addOption(document.formID.lga,"Bade","Bade")
addOption(document.formID.lga,"Gujba","Gujba")
addOption(document.formID.lga,"Gulani","Gulani")
addOption(document.formID.lga,"Fika","Fika")
addOption(document.formID.lga,"Fune","Fune")
addOption(document.formID.lga,"Jakusko","Jakusko")
addOption(document.formID.lga,"Karasuwa","Karasuwa")
addOption(document.formID.lga,"Machina","Machina")
addOption(document.formID.lga,"Nangere","Nangere")
addOption(document.formID.lga,"Nguru","Nguru")
addOption(document.formID.lga,"Potiskum","Potiskum")
addOption(document.formID.lga,"Tarmuwa","Tarmuwa")
addOption(document.formID.lga,"Yunusari","Yunusari")
addOption(document.formID.lga,"Yusufari","Yusufari")
}

if(document.formID.state.value == 'Zamfara'){
addOption(document.formID.lga,"Anka","Anka");
addOption(document.formID.lga,"Bakura","Bakura")
addOption(document.formID.lga,"Birnin Magaji/Kiyaw","Birnin Magaji/Kiyaw");
addOption(document.formID.lga,"Bukkuyum","Bukkuyum")
addOption(document.formID.lga,"Bungudu","Bungudu");
addOption(document.formID.lga,"Chafe","Chafe")
addOption(document.formID.lga,"Gummi","Gummi");
addOption(document.formID.lga,"Gusau","Gusau")
addOption(document.formID.lga,"Kaura Namoda","Kaura Namoda");
addOption(document.formID.lga,"Maradun","Maradun")
addOption(document.formID.lga,"Maru","Maru");
addOption(document.formID.lga,"Shinkafi","Shinkafi")
addOption(document.formID.lga,"Talata Mafara","Talata Mafara");
addOption(document.formID.lga,"Zurmi","Zurmi");
}
}


//////////////////
function removeAllOptions(selectbox)
{
	var i;
	for(i=selectbox.options.length-1;i>=0;i--)
	{
		//selectbox.options.remove(i);
		selectbox.remove(i);
	}
}


function addOption(selectbox, value, text )
{
	var optn = document.createElement("OPTION");
	optn.text = text;
	optn.value = value;

	selectbox.options.add(optn);
}
