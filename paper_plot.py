#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import scienceplots
import matplotlib.colors as mcolors

plt.style.use(['science', 'nature'])

plt.rcParams['axes.prop_cycle'] = plt.cycler('color', ['#0085CA', '#008F00', '#FF9500', '#FF2C00', '#845B97', '#474747', '#9e9e9e', mcolors.CSS4_COLORS["salmon"]])

plt.rcParams['font.size'] = 11
plt.rcParams['xtick.minor.visible'] = False
plt.rcParams['ytick.minor.visible'] = False
plt.rcParams['axes.linewidth'] = 0.5
plt.rcParams['axes.labelsize'] =  11
plt.rcParams['axes.labelsize'] =  11
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11


import numpy as np
def merge(x,y):
    return (np.array([x,y]).T).flatten()

def double(x):
    return (np.array([x,x]).T).flatten()


# figure width and ratio
fw=4
gr=4/3
# transparency
trans=0.5
# hatched bands
hl=["\\\\","//",  "+"]


def plot_pp_spectra_5020GeV(tag="./plots/fig_pp_5020GeV_hadron_spectra_y0.8"):
    fig, axs = plt.subplots(2, 1, figsize=(fw,fw), sharex=True,height_ratios=[2,1])
    row=0
    cols=['tab:green', 'tab:purple', 'tab:brown', 'tab:olive']
    cols2=['tab:red', 'tab:blue', 'tab:orange']
    cols=['tab:red', 'tab:cyan', 'tab:olive', 'tab:brown', 'tab:olive']
    FFlist=["BKK", "NNFF11_HadronSum_nlo", "NPC23_CHHAsum_nlo"]
    FFlabel=["NLO scale", "NNFF11",  "NPC23"]
    for i, FF in enumerate(FFlist):
        fname = "./data/int_ALICE_pp_FF_ref_5020GeV_CT18ANLO_%s_spectra.txt" % FF
        data=np.loadtxt(fname)
        pTm=data[:,0]
        Npoints=len(pTm)
        pTp=data[:,1]
        pTc=data[:,2]

        pTd = merge(pTm,pTp)
        if i==0:
            yc =  double(data[:,6])
            ym =  double(data[:,7])
            yp =  double(data[:,8])
            LOym =  double(data[:,4])
            LOyp =  double(data[:,5])
        else:
            yc =  double(data[:,8])
            ym =  double(data[:,11])
            yp =  double(data[:,12])
            #ym =  double(data[:,7])
            #yp =  double(data[:,8])
        ax=axs[0]
        if i==0:
            ax.fill_between(pTd,LOym, LOyp, facecolor='tab:brown', edgecolor='none', alpha=trans, label='LO scale')
        ax.plot(pTd,yc, color=cols[i])
        ax.fill_between(pTd,ym, yp, facecolor=cols[i], edgecolor='none', alpha=trans, label=FFlabel[i])
        

        ax=axs[1]
        if i ==0:
            yref=yc
            ycref=data[:,6]
        if i==0:
            ax.fill_between(pTd,LOym/yref, LOyp/yref, edgecolor='none', facecolor='tab:brown', alpha=trans)
        ax.plot(pTd,yc/yref, color=cols[i])
        ax.fill_between(pTd,ym/yref, yp/yref, edgecolor='none', facecolor=cols[i], alpha=trans)

    if True:
        fname = "./data/ALICE_5.02TeV_hadron_spectra.csv"

        data=np.loadtxt(fname)
        pTc=data[-Npoints:,0]
        pTm=data[-Npoints:,1]
        pTp=data[-Npoints:,2]
        sg=67.3 #mb
        data[-Npoints:,3:] *= (sg/(2*np.pi*pTc))[-Npoints:,np.newaxis]

        pTd = merge(pTm,pTp)
        yc =  double(data[-Npoints:,3])
        ym =  double(data[-Npoints:,3]+data[-Npoints:,6])
        yp =  double(data[-Npoints:,3]+data[-Npoints:,7])
        ax=axs[0]
        ax.plot(pTd,yc, color='k')
        ax.errorbar(pTc,data[-Npoints:,3], yerr=np.abs(data[-Npoints:,4:6]).T, color='k', capsize=5, fmt='o', label='ALICE stat.')
        ax.fill_between(pTd,ym, yp, edgecolor='none',facecolor='k', alpha=trans, label='ALICE sys.')
        ax=axs[1]
        ax.errorbar(pTc,data[-Npoints:,3]/ycref, yerr=np.abs(data[-Npoints:,4:6]/ycref[:,np.newaxis]).T, color='k', capsize=5, fmt='o', label='ALICE stat.')
        ax.plot(pTd,yc/yref, color='k')
        ax.fill_between(pTd,ym/yref, yp/yref, edgecolor='none',facecolor='k', alpha=trans)

    axs[0].set_yscale('log')
    axs[0].set_xscale('log')
    axs[0].set_ylabel("$\\frac{d\\sigma^h}{2\\pi p_T dp_T dy}$ [mb/GeV$^2$]")
    axs[1].set_xscale('log')
    ticks=[int(np.round(pT)) for pT in pTm]+[int(np.round(pTp[-1]))]
    axs[1].set_xlim([pTm[0],pTp[-1]])
    axs[1].set_xticks([])
    axs[1].set_xticks(ticks, ticks)
    axs[1].set_ylim([0.5,1.5])
    yticks=[0.60, 0.80, 1.0, 1.2, 1.40]
    axs[1].set_yticks(yticks, yticks)
    plt.minorticks_off()
    axs[1].set_xlabel("hadron $p_T$ [GeV]")
    axs[1].set_ylabel("ratio to BKK")


    axs[0].set_ylim([1.1e-8, 2e-3])   
    axs[0].legend(frameon=False, ncols=1, columnspacing=0.5, loc="upper right", labelspacing=0.2, handlelength=2)
    axs[0].set_title('$pp$ $\\sqrt{s}=5.02$ TeV $\\sigma_\\mathrm{NN}=67.3$ mb, $|y_h|<0.8$')
    plt.tight_layout()
    plt.subplots_adjust(hspace=0)
    plt.savefig("%s.pdf" % tag)
    
def plot_pp_spectra_5360GeV(tag="./plot/fig_pp_5360GeV_hadron_spectra_y0.8", ymax=0.8, maintag="ALICE"):
    fig, axs = plt.subplots(2, 1, figsize=(fw,fw), sharex=True,height_ratios=[2,1])
    row=0
    cols=['tab:cyan', 'tab:olive']
    cols2=['tab:red', 'tab:blue', 'tab:orange']
    PDFlist=["CT18ANLO", "TUJU21_nlo_1_1", "nNNPDF30_nlo_as_0118_p"]
    PDFlabel=["CT18ANLO", "TUJU21", "nNNPDF30"]
    for i, PDF in enumerate(PDFlist):
        fname = "./data/%s_OO_PDF_5360GeV_%s_BKK_PDF_spectra.txt" % (maintag, PDF)
        data=np.loadtxt(fname)
        pTc=data[:,0]
        yc=data[:,6]
        ym=data[:,9]
        yp=data[:,10]
        yms=data[:,7]
        yps=data[:,8]

        LOyc=data[:,1]
        LOyms=data[:,2]
        LOyps=data[:,3]

        ax=axs[0]
        if i==0:
            ax.fill_between(pTc,LOyms, LOyps, facecolor='tab:brown',edgecolor='none', alpha=trans, label="LO scale")
            ax.fill_between(pTc,yms, yps, facecolor=cols2[i],edgecolor='none', alpha=trans, label="NLO scale")
        ax.plot(pTc,yc, color=cols2[i])
        ax.fill_between(pTc,ym, yp, edgecolor=cols2[i],facecolor='none', hatch=hl[i], label=PDFlabel[i])

        ax=axs[1]
        if i ==0:
            yref=yc
        if i==0:
            ax.fill_between(pTc,LOyms/yref, LOyps/yref, facecolor='tab:brown', edgecolor='none', alpha=trans, label="")
            ax.fill_between(pTc,yms/yref, yps/yref, facecolor=cols2[i], edgecolor='none', alpha=trans, label="")
        ax.plot(pTc,yc/yref, color=cols2[i])
        ax.fill_between(pTc,ym/yref, yp/yref,facecolor='none', edgecolor=cols2[i], hatch=hl[i])




    FFlist=["NNFF11_HadronSum_nlo", "NPC23_CHHAsum_nlo"]
    FFlabel=["NNFF11", "NPC23"]
    for i, FF in enumerate(FFlist):

        fname = "./data/%s_OO_FF_err_5360GeV_CT18ANLO_%s_FF_spectra.txt" % (maintag, FF)
        data=np.loadtxt(fname)
        pTc=data[:,0]
        yc=data[:,6]
        ym=data[:,9]
        yp=data[:,10]
        yms=data[:,7]
        yps=data[:,8]

        ax=axs[0]
        ax.plot(pTc,yc, color=cols[i])
        ax.fill_between(pTc,ym, yp, edgecolor='none',facecolor=cols[i], alpha=trans, label=FFlabel[i])

        ax=axs[1]
        ax.plot(pTc,yc/yref, color=cols[i])
        ax.fill_between(pTc,ym/yref, yp/yref, facecolor=cols[i],edgecolor='none', alpha=trans)
        

    axs[0].set_yscale('log')
    plt.minorticks_on()
    axs[0].set_xscale('log')
    axs[0].set_ylabel("$\\frac{d\\sigma^h}{2\\pi p_T dp_T dy}$ [mb/GeV$^2$]")
    axs[1].set_xscale('log')
    ticks=[4,6,10,20,40,70,120,200]
    axs[1].set_xlim([pTc[0],pTc[-1]])
    axs[1].set_ylim([0.5,1.5])
    yticks=[0.60, 0.80, 1.0, 1.2, 1.40]
    axs[1].set_yticks(yticks, yticks)
    plt.minorticks_on()
    axs[1].set_xticks(ticks, ticks)
    axs[1].set_xlabel("hadron $p_T$ [GeV]")
    axs[1].set_ylabel("ratio to BKK")

    axs[0].legend(frameon=False, ncols=1, columnspacing=0.5, loc="upper right", labelspacing=0.2, handlelength=2, bbox_to_anchor=(1.03,1.03))
    axs[0].set_title('$pp$ $\\sqrt{s}=5.36$ TeV, \\quad  $|y_h|<%g$' % ymax)
    plt.tight_layout()
    plt.subplots_adjust(hspace=0)
    #plt.savefig("%s.pdf" % tag)

def plot_OO_spectra_5360GeV(tag="./plots/fig_OO_5360GeV_hadron_spectra_y0.8", ymax=0.8, maintag="ALICE"):
    fig, axs = plt.subplots(2, 1, figsize=(fw,fw), sharex=True,height_ratios=[2,1])
    row=0
    cols=['tab:cyan', 'tab:olive']
    cols2=['tab:red', 'tab:blue', 'tab:orange']
    PDFlist=["EPPS21nlo_CT18Anlo_O16", "TUJU21_nlo_16_8", "nNNPDF30_nlo_as_0118_A16_Z8"]
    PDFlabel=["EPPS21", "TUJU21", "nNNPDF30"]
    for i, PDF in enumerate(PDFlist):
        fname = "./data/%s_OO_PDF_5360GeV_%s_BKK_PDF_spectra.txt" % (maintag, PDF)
        #fname = "%s_ALICE.txt" % PDF
        data=np.loadtxt(fname)
        pTc=data[:,0]
        yc=data[:,6]
        ym=data[:,9]
        yp=data[:,10]
        yms=data[:,7]
        yps=data[:,8]

        LOyc=data[:,1]
        LOyms=data[:,2]
        LOyps=data[:,3]
        ax=axs[0]
        if i==0:
            ax.fill_between(pTc,LOyms, LOyps, facecolor='tab:brown',edgecolor='none', alpha=trans, label="LO scale")
            ax.fill_between(pTc,yms, yps, facecolor=cols2[i],edgecolor='none', alpha=trans, label="NLO scale")
        ax.plot(pTc,yc, color=cols2[i])
        ax.fill_between(pTc,ym, yp, edgecolor=cols2[i],facecolor='none', hatch=hl[i], label=PDFlabel[i])

        ax=axs[1]
        if i ==0:
            yref=yc
        if i==0:
            ax.fill_between(pTc,LOyms/yref, LOyps/yref, facecolor='tab:brown', edgecolor='none', alpha=trans, label="")
            ax.fill_between(pTc,yms/yref, yps/yref, facecolor=cols2[i], edgecolor='none', alpha=trans, label="")
        ax.plot(pTc,yc/yref, color=cols2[i])
        ax.fill_between(pTc,ym/yref, yp/yref,facecolor='none', edgecolor=cols2[i], hatch=hl[i])




    FFlist=["NNFF11_HadronSum_nlo", "NPC23_CHHAsum_nlo"]
    FFlabel=["NNFF11", "NPC23"]
    for i, FF in enumerate(FFlist):

        fname = "./data/%s_OO_FF_err_5360GeV_EPPS21nlo_CT18Anlo_O16_%s_FF_spectra.txt" % (maintag, FF)
        data=np.loadtxt(fname)
        pTc=data[:,0]
        yc=data[:,6]
        ym=data[:,9]
        yp=data[:,10]
        yms=data[:,7]
        yps=data[:,8]

        ax=axs[0]
        ax.plot(pTc,yc, color=cols[i])
        ax.fill_between(pTc,ym, yp, color=cols[i], alpha=trans, label=FFlabel[i])
        ax.fill_between(pTc,ym, yp, edgecolor=cols[i], facecolor='none', label="")

        ax=axs[1]
        ax.plot(pTc,yc/yref, color=cols[i])
        ax.fill_between(pTc,ym/yref, yp/yref, color=cols[i], alpha=trans)
        ax.fill_between(pTc,ym/yref, yp/yref, edgecolor=cols[i], facecolor='none', label="")
        

    axs[0].set_yscale('log')
    plt.minorticks_on()
    axs[0].set_xscale('log')
    axs[0].set_ylabel("$\\frac{d\\sigma^h}{2\\pi p_T dp_T dy}/A^2$ [mb/GeV$^2$]")
    axs[1].set_xscale('log')
    ticks=[4,6,10,20,40,70,120,200]
    axs[1].set_xlim([pTc[0],pTc[-1]])
    axs[1].set_ylim([0.5,1.5])
    yticks=[0.60, 0.80, 1.0, 1.2, 1.40]
    axs[1].set_yticks(yticks, yticks)
    axs[1].set_xticks(ticks, ticks)
    axs[1].set_xlabel("hadron $p_T$ [GeV]")
    axs[1].set_ylabel("ratio to BKK")

    axs[0].legend(frameon=False, ncols=1, columnspacing=0.5, loc="upper right", labelspacing=0.2, handlelength=2, bbox_to_anchor=(1.03,1.03))
    axs[0].set_title('OO $\\sqrt{s_\\text{NN}}=5.36$ TeV, \\quad  $|y_h|<%g$' % ymax)
    plt.tight_layout()
    plt.subplots_adjust(hspace=0)
    plt.savefig("%s.pdf" % tag)  

def plot_RAA(tag="./plots/fig_OO_pp_5360GeV_hadron_RAA_y0.8", maintag="ALICE", ymax=0.8):
    fig, axs = plt.subplots(1, 1, figsize=(fw,fw/gr))

    row=0
    cols=['tab:cyan', 'tab:olive']
    cols2=['tab:red', 'tab:blue', 'tab:orange']
    trans=0.5


    PDFlist=["EPPS21nlo_CT18Anlo_O16_CT18ANLO", "TUJU21_nlo_16_8_TUJU21_nlo_1_1", "nNNPDF30_nlo_as_0118_A16_Z8_nNNPDF30_nlo_as_0118_p"]
    PDFlabel=["EPPS21", "TUJU21", "nNNPDF30"]
    for i, PDF in enumerate(PDFlist):
        fname = "./data/%s_OO_PDF_5360GeV_%s_BKK_PDF_ratio.txt" % (maintag, PDF)
        data=np.loadtxt(fname)
        pTc=data[:,0]
        yc=data[:,6]
        ym=data[:,9]
        yp=data[:,10]
        yms=data[:,7]
        yps=data[:,8]
        LOyc=data[:,1]
        LOyms=data[:,2]
        LOyps=data[:,3]

        ax=axs
        ax.plot(pTc,yc, color=cols2[i])
        if i==0:
            ax.fill_between(pTc,LOyms, LOyps, edgecolor='none',facecolor='tab:brown', alpha=trans, label="LO scale")
            ax.fill_between(pTc,yms, yps, edgecolor='none',facecolor=cols2[i], alpha=trans, label="NLO scale")
        ax.fill_between(pTc,ym, yp, edgecolor=cols2[i],facecolor='none', hatch=hl[i], label=PDFlabel[i])

    FFlist=[ "NNFF11_HadronSum_nlo", "NPC23_CHHAsum_nlo"]
    FFlabel=["NNFF11", "NPC23"]
    for i, FF in enumerate(FFlist):

        fname = "./data/%s_OO_FF_err_5360GeV_EPPS21nlo_CT18Anlo_O16_CT18ANLO_%s_FF_ratio.txt" % (maintag, FF)
        data=np.loadtxt(fname)
        pTc=data[:,0]
        yc=data[:,6]
        ym=data[:,9]
        yp=data[:,10]
        # leading order scale
        LOyc=data[:,1]
        LOyms=data[:,2]
        LOyps=data[:,3]

        ax=axs
        ax.plot(pTc,yc, color=cols[i])
        ax.fill_between(pTc,ym, yp, edgecolor='none',facecolor=cols[i], alpha=trans, label=FFlabel[i])

    for i, PDF in enumerate(PDFlist[:1]):
        fname = "./data/%s_OO_PDF_5360GeV_%s_BKK_PDF_ratio.txt" % (maintag, PDF)
        #fname = "%s_ALICE.txt" % PDF
        data=np.loadtxt(fname)
        pTc=data[:,0]
        yc=data[:,6]
        ym=data[:,9]
        yp=data[:,10]
        yms=data[:,7]
        yps=data[:,8]
        LOyc=data[:,1]
        LOyms=data[:,2]
        LOyps=data[:,3]

        ax=axs
        ax.plot(pTc,yc, color=cols2[i])
        ax.fill_between(pTc,ym, yp, edgecolor=cols2[i],facecolor='none', hatch=hl[i], label="")

    fname2 = "./data/ALICE_OO_pi0_SCALE_5360GeV_EPPS21nlo_CT18Anlo_O16_CT18ANLO_NPC23_PI0_nlo_SCALE_ratio.txt"
    data_pi0=np.loadtxt(fname2)
    pi0yc=data_pi0[:,4]
    pi0yms=data_pi0[:,5]
    pi0yps=data_pi0[:,6]
    ax.plot(pTc,pi0yc, 'k--', label="$\\pi^0$")
    axs.set_xscale('log')
    axs.hlines(1,4,200, 'k')
    axs.set_ylabel("$R^h_{AA}$")
    axs.set_ylim([0.65,1.30])
    #axs[1].set_xscale('log')
    ticks=[4,6,10,20,40,70,120,200]
    axs.set_xlim([pTc[0],pTc[-1]])
    #axs[1].set_ylim([0.85,1.15])
    axs.set_xticks(ticks, ticks)
    axs.set_yticks([0.70+i*0.10 for i in range(7)])
    axs.set_xlabel("hadron $p_T$ [GeV]")
    #axs[0].set_ylabel("ratio to BKK")

    axs.legend(frameon=False, ncols=2, columnspacing=0.5, loc="upper left", labelspacing=0.2, handlelength=2,bbox_to_anchor=(0,1.02))
    axs.set_title('OO/$pp$ $\\sqrt{s_\\text{NN}}=5.36$ TeV, \\quad  $|y_h|<%g$' % ymax)
    plt.tight_layout()
    #plt.subplots_adjust(hspace=0)
    plt.savefig("%s.pdf" % tag) 

def plot_RAA_ALICE(tag="./plots/fig_ALICE_RAA", maintag="ALICE", ymax=0.8):
    fig, axs = plt.subplots(1, 1, figsize=(fw,fw/gr))

    row=0
    cols=['tab:green', 'tab:purple']
    cols2=['tab:red', 'tab:blue', 'tab:orange']
    trans=0.5


    PDFlist=["EPPS21nlo_CT18Anlo_O16_CT18ANLO"]
    PDFlabel=["EPPS21"]
    for i, PDF in enumerate(PDFlist):
        fname = "./data/%s_OO_PDF_5360GeV_%s_BKK_PDF_ratio.txt" % (maintag, PDF)
        #fname = "%s_ALICE.txt" % PDF
        data=np.loadtxt(fname)
        pTc=data[:,0]
        yc=data[:,6]
        ym=data[:,9]
        yp=data[:,10]
        yms=data[:,7]
        yps=data[:,8]
        LOyc=data[:,1]
        LOyms=data[:,2]
        LOyps=data[:,3]

        ax=axs
        ax.plot(pTc,LOyc, color='tab:brown')
        ax.plot(pTc,yc, color=cols2[i])
        if i==0:
            ax.fill_between(pTc,LOyms, LOyps, color='tab:brown', alpha=trans, label="BKK LO scale")
            ax.fill_between(pTc,LOyms, LOyps, edgecolor='tab:brown', facecolor='none', label="")
            ax.fill_between(pTc,yms, yps, color=cols2[i], alpha=trans, label="BKK NLO scale")
            ax.fill_between(pTc,yms, yps, edgecolor=cols2[i], facecolor='none', label="")
        #ax.fill_between(pTc,yms, yps, color=cols2[i], alpha=trans, label="")
        ax.fill_between(pTc,ym, yp, edgecolor=cols2[i],facecolor='none', hatch=hl[i], label=PDFlabel[i])

    axs.set_xscale('log')
    axs.hlines(1,4,200, 'k')
    axs.set_ylabel("$R^h_{AA}$")
    axs.set_ylim([0.65,1.25])
    #axs[1].set_xscale('log')
    ticks=[4,6,10,20,40,70,120,200]
    axs.set_xlim([pTc[0],pTc[-1]])
    #axs[1].set_ylim([0.85,1.15])
    axs.set_xticks(ticks, ticks)
    axs.set_xlabel("hadron $p_T$ [GeV]")
    #axs[0].set_ylabel("ratio to BKK")

    axs.legend(frameon=False, ncols=2, columnspacing=0.5, loc="upper left", labelspacing=0.2, handlelength=2)
    axs.set_title('OO/$pp$ $\\sqrt{s_\\text{NN}}=5.36$ TeV, \\quad  $|y_h|<%g$' % ymax)
    plt.tight_layout()
    #plt.subplots_adjust(hspace=0)
    plt.savefig("%s.pdf" % tag)  

def plot_RAA_CMS(tag="./plots/fig_CMS_RAA", maintag="CMS", ymax=1):
    fig, axs = plt.subplots(1, 1, figsize=(fw,fw/gr))
    #fig, axs = plt.subplots(2, 1, figsize=(fw,1.5*fw/gr), sharex=True,height_ratios=[3,1])

    row=0
    cols=['tab:green', 'tab:purple']
    cols2=['tab:red', 'tab:blue', 'tab:orange']
    trans=0.5


    PDFlist=["EPPS21nlo_CT18Anlo_O16_CT18ANLO"]
    PDFlabel=["EPPS21"]
    for i, PDF in enumerate(PDFlist):
        fname = "./data/%s_OO_PDF_5360GeV_%s_BKK_PDF_ratio.txt" % (maintag, PDF)
        #fname = "%s_ALICE.txt" % PDF
        data=np.loadtxt(fname)
        pTc=data[:,0]
        yc=data[:,6]
        ym=data[:,9]
        yp=data[:,10]
        yms=data[:,7]
        yps=data[:,8]
        LOyc=data[:,1]
        LOyms=data[:,2]
        LOyps=data[:,3]

        ax=axs
        ax.plot(pTc,LOyc, color='tab:brown')
        ax.plot(pTc,yc, color=cols2[i])
        if i==0:
            ax.fill_between(pTc,LOyms, LOyps, color='tab:brown', alpha=trans, label="BKK LO scale")
            ax.fill_between(pTc,LOyms, LOyps, edgecolor='tab:brown', facecolor='none', label="")
            ax.fill_between(pTc,yms, yps, color=cols2[i], alpha=trans, label="BKK NLO scale")
            ax.fill_between(pTc,yms, yps, edgecolor=cols2[i], facecolor='none', label="")
        #ax.fill_between(pTc,yms, yps, color=cols2[i], alpha=trans, label="")
        ax.fill_between(pTc,ym, yp, edgecolor=cols2[i],facecolor='none', hatch=hl[i], label=PDFlabel[i])

    axs.set_xscale('log')
    axs.hlines(1,4,200, 'k')
    axs.set_ylabel("$R^h_{AA}$")
    axs.set_ylim([0.65,1.25])
    #axs[1].set_xscale('log')
    ticks=[4,6,10,20,40,70,120,200]
    axs.set_xlim([pTc[0],pTc[-1]])
    #axs[1].set_ylim([0.85,1.15])
    axs.set_xticks(ticks, ticks)
    axs.set_xlabel("hadron $p_T$ [GeV]")
    #axs[0].set_ylabel("ratio to BKK")

    axs.legend(frameon=False, ncols=2, columnspacing=0.5, loc="upper left", labelspacing=0.2, handlelength=2)
    axs.set_title('OO/$pp$ $\\sqrt{s_\\text{NN}}=5.36$ TeV, \\quad  $|y_h|<%g$' % ymax)
    plt.tight_layout()
    #plt.subplots_adjust(hspace=0)
    plt.savefig("%s.pdf" % tag)  
def plot_RAA_ATLAS(tag="./plots/fig_ATLAS_RAA", maintag="ATLAS", ymax=2.5):
    fig, axs = plt.subplots(1, 1, figsize=(fw,fw/gr))
    #fig, axs = plt.subplots(2, 1, figsize=(fw,1.5*fw/gr), sharex=True,height_ratios=[3,1])

    row=0
    cols=['tab:green', 'tab:purple']
    cols2=['tab:red', 'tab:blue', 'tab:orange']


    PDFlist=["EPPS21nlo_CT18Anlo_O16_CT18ANLO"]
    PDFlabel=["EPPS21"]
    for i, PDF in enumerate(PDFlist):
        fname = "./data/%s_OO_PDF_5360GeV_%s_BKK_PDF_ratio.txt" % (maintag, PDF)
        #fname = "%s_ALICE.txt" % PDF
        data=np.loadtxt(fname)
        pTc=data[:,0]
        yc=data[:,6]
        ym=data[:,9]
        yp=data[:,10]
        yms=data[:,7]
        yps=data[:,8]
        LOyc=data[:,1]
        LOyms=data[:,2]
        LOyps=data[:,3]

        ax=axs
        ax.plot(pTc,LOyc, color='tab:brown')
        ax.plot(pTc,yc, color=cols2[i])
        if i==0:
            ax.fill_between(pTc,LOyms, LOyps, color='tab:brown', alpha=trans, label="BKK LO scale")
            ax.fill_between(pTc,LOyms, LOyps, edgecolor='tab:brown', facecolor='none', label="")
            ax.fill_between(pTc,yms, yps, color=cols2[i], alpha=trans, label="BKK NLO scale")
            ax.fill_between(pTc,yms, yps, edgecolor=cols2[i], facecolor='none', label="")
        #ax.fill_between(pTc,yms, yps, color=cols2[i], alpha=trans, label="")
        ax.fill_between(pTc,ym, yp, edgecolor=cols2[i],facecolor='none', hatch=hl[i], label=PDFlabel[i])

    axs.set_xscale('log')
    axs.hlines(1,4.15,85, 'k')
    axs.set_ylabel("$R^h_{AA}$")
    axs.set_ylim([0.65,1.25])
    #axs[1].set_xscale('log')
    ticks=[5,6,10,15,20,40,60, 85]
    axs.set_xlim([pTc[0],pTc[-1]])
    #axs[1].set_ylim([0.85,1.15])
    axs.set_xticks(ticks, ticks)
    axs.set_xlabel("hadron $p_T$ [GeV]")
    #axs[0].set_ylabel("ratio to BKK")

    axs.legend(frameon=False, ncols=2, columnspacing=0.5, loc="upper left", labelspacing=0.2, handlelength=2)
    axs.set_title('OO/$pp$ $\\sqrt{s_\\text{NN}}=5.36$ TeV, \\quad  $|y_h|<%g$' % ymax)
    plt.tight_layout()
    #plt.subplots_adjust(hspace=0)
    plt.savefig("%s.pdf" % tag)  
def plot_RAA_ONe(tag="./plots/fig_NeNe_OO_RAA", maintag="ALICE", ymax=0.8):
    fig, axs = plt.subplots(1, 1, figsize=(fw,fw/gr))
    #fig, axs = plt.subplots(2, 1, figsize=(fw,1.5*fw/gr), sharex=True,height_ratios=[3,1])

    row=0
    cols=['tab:green', 'tab:purple']
    cols2=['tab:red', 'tab:blue', 'tab:orange']


    PDFlist=["EPPS21nlo_CT18Anlo_O16"]
    PDFlabel=["EPPS21"]
    for i, PDF in enumerate(PDFlist):
        fname = "./data/%s_NeNe_PDF_5360GeV_%s_%s_BKK_PDF_ONe_ratio.txt" % (maintag,"EPPS21nlo_CT18Anlo_Ne20", PDF)
        #fname = "%s_ALICE.txt" % PDF
        data=np.loadtxt(fname)
        pTc=data[:,0]
        yc=data[:,6]
        ym=data[:,9]
        yp=data[:,10]
        yms=data[:,7]
        yps=data[:,8]
        LOyc=data[:,1]
        LOyms=data[:,2]
        LOyps=data[:,3]

        ax=axs
        ax.plot(pTc,LOyc, color='tab:brown')
        ax.plot(pTc,yc, color=cols2[i])
        if i==0:
            ax.fill_between(pTc,LOyms, LOyps, color='tab:brown', alpha=trans, label="BKK LO scale")
            ax.fill_between(pTc,LOyms, LOyps, edgecolor='tab:brown', facecolor='none', label="")
            ax.fill_between(pTc,yms, yps, color=cols2[i], alpha=trans, label="BKK NLO scale")
            ax.fill_between(pTc,yms, yps, edgecolor=cols2[i], facecolor='none', label="")
        #ax.fill_between(pTc,yms, yps, color=cols2[i], alpha=trans, label="")
        ax.fill_between(pTc,ym, yp, edgecolor=cols2[i],facecolor='none', hatch=hl[i], label=PDFlabel[i])

    axs.set_xscale('log')
    axs.hlines(1,4.15,85, 'k')
    axs.set_ylabel("$R^h_{AA}$")
    axs.set_ylim([0.95,1.05])
    #axs[1].set_xscale('log')
    ticks=[4,6,10,20,40,70,120,200]
    axs.set_xlim([pTc[0],pTc[-1]])
    #axs[1].set_ylim([0.85,1.15])
    axs.set_xticks(ticks, ticks)
    axs.set_xlabel("hadron $p_T$ [GeV]")
    #axs[0].set_ylabel("ratio to BKK")

    axs.legend(frameon=False, ncols=2, columnspacing=0.5, loc="upper left", labelspacing=0.2, handlelength=2)
    axs.set_title('NeNe/OO $\\sqrt{s_\\text{NN}}=5.36$ TeV,  $|y_h|<%g$' % ymax)
    plt.tight_layout()
    #plt.subplots_adjust(hspace=0)
    plt.savefig("%s.pdf" % tag) 
def plot_isospin_RAA(tag="./plots/fig_RAA_isospin_test"):
    fig, axs = plt.subplots(1, 1, figsize=(fw,fw/gr))
    cols=['tab:cyan', 'tab:olive', 'tab:orange', 'tab:pink', 'tab:green',  'tab:purple', 'tab:brown', 'tab:blue']
    FFlist=["NNFF11_HadronSum_nlo" ,"NPC23_CHHAsum_nlo"]
    FFlabel=["NNFF11" ,"NPC23"]

    ax=axs
    width=1
    for i,FF in enumerate(FFlist):
        if FF=="NNFF10":
            for j,p in enumerate(["PI", "KA", "PR"]):
                FF2="NNFF10_%ssum_nlo" % p
                fnamepp="./data_LO/ALICE_OO_NNFF_5360GeV_CT18ANLO_0_CT18ANLO_0_%s_0_muF_1.0_muR_1.0_muFF_1.0_result.out" % FF2
                fnameOO="./data_LO/ALICE_OO_NNFF_5360GeV_EPPS21nlo_CT18Anlo_O16_0_EPPS21nlo_CT18Anlo_O16_0_%s_0_muF_1.0_muR_1.0_muFF_1.0_result.out" % FF2
                datap=np.loadtxt(fnamepp)
                dataO=np.loadtxt(fnameOO)
                pT = datap[:,0]
                if j==0:
                    yp = datap[:,1]
                    yO = dataO[:,1]
                else:
                    yp += datap[:,1]
                    yO += dataO[:,1]
        else:
            fnamepp="./data_LO/ALICE_OO_NNFF_5360GeV_CT18ANLO_0_CT18ANLO_0_%s_0_muF_1.0_muR_1.0_muFF_1.0_result.out" % FF
            fnameOO="./data_LO/ALICE_OO_NNFF_5360GeV_EPPS21nlo_CT18Anlo_O16_0_EPPS21nlo_CT18Anlo_O16_0_%s_0_muF_1.0_muR_1.0_muFF_1.0_result.out" % FF
            datap=np.loadtxt(fnamepp)
            dataO=np.loadtxt(fnameOO)
            pT = datap[:,0]
            yp = datap[:,1]
            yO = dataO[:,1]
        if i==0:
            ypref=yp
            yOref=yO
        ax.plot(pT,yO/yp, label=FFlabel[i],lw=width, color=cols[i])

    for i,FF in enumerate(["NNFF11_HadronSum_nlo" ,"NPC23_CHHAsum_nlo"]):
        fname = "./data_LO/FF_iso_check_5360GeV_CT18ANLO_0_%s_0_muR_1.0_muF_1.0_muFF_1.0.out" % FF
        datap=np.loadtxt(fname)
        fname = "./data_LO/FF_iso_check_5360GeV_EPPS21nlo_CT18Anlo_O16_0_%s_0_muR_1.0_muF_1.0_muFF_1.0.out" % FF
        dataO=np.loadtxt(fname)
        if i==0:
            ax.plot(pT, (dataO[:,3])/datap[:,3], label='$D_d^h=D_u^h$', ls=':',lw=1.5, color='k')      
        ax.plot(pT, (dataO[:,3])/datap[:,3], label='', ls=':',lw=1.5, color=cols[i])    
    for i,FF in enumerate(["NNFF11_HadronSum_nlo" ,"NPC23_CHHAsum_nlo"]):
        fname = "./data_LO/FF_antiiso_check_5360GeV_CT18ANLO_0_%s_0_muR_1.0_muF_1.0_muFF_1.0.out" % FF
        datap=np.loadtxt(fname)
        fname = "./data_LO/FF_antiiso_check_5360GeV_EPPS21nlo_CT18Anlo_O16_0_%s_0_muR_1.0_muF_1.0_muFF_1.0.out" % FF
        dataO=np.loadtxt(fname)
        if i==0:
            ax.plot(pT, (dataO[:,3])/datap[:,3], label='$D_d^h=0$', ls='--',lw=1.5, color='k')      
        ax.plot(pT, (dataO[:,3])/datap[:,3], label='', ls='--',lw=1.5, color=cols[i])      
    ax.set_xscale('log')
    ax.hlines(1,4,200, 'k')
    ax.set_ylabel("$R^h_{AA}$")
    ax.set_ylim([0.7,1.1])
    ticks=[4,6,10,20,40,70,120,200]
    ax.set_xlim([pT[0],pT[-1]])
    #axs[1].set_ylim([0.85,1.15])
    ax.set_xticks(ticks, ticks)
    ax.set_xlabel("hadron $p_T$ [GeV]")

    ax.legend(frameon=False, ncols=2, columnspacing=0.5, loc="lower right", labelspacing=0.2, handlelength=2, title="Leading Order")
    ax.set_title('OO/$pp$ $\\sqrt{s}=5.36$ TeV, \\quad  $|y_h|<%g$' % 0.8)
    plt.tight_layout()
    #plt.grid(True)
    plt.subplots_adjust(hspace=0)
    plt.savefig("%s.pdf" % tag) 
def plot_FF(tag="./plots/fig_FF"):
    fig, axs = plt.subplots(1, 1, figsize=(fw,fw/gr))
    cols=['tab:cyan', 'tab:olive', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

    FFlist=["NNFF11_HadronSum_nlo","NPC23_CHHAsum_nlo"]
    FFlabel=["NNFF11", "NPC23"]
    ax=axs
    part=['g', 'd', 'u', 's'] 
    #yref={}
    for i,FF in enumerate(FFlist):
        fname="./data_LO/%s_xf_Q_100.0.out" % FF
        data=np.loadtxt(fname)
        x = data[:,0]
        for j,pos in enumerate([1, 2]):
            yc = data[:,1+pos*3]
            ym = data[:,2+pos*3]
            yp = data[:,3+pos*3]
            
            if j==0:
                ax.plot(x,x**2*yc, label='', color=cols[i], ls='-')
                ax.fill_between(x,x**2*(yc-ym), x**2*(yc+yp), label=FFlabel[i], edgecolor='none',facecolor=cols[i],alpha=0.5)
                if i==1:
                    ax.plot(x,x**2*yc, label='$d$', color='k', ls='-')
                    ax.plot(x,x**2*yc, label='$u$', color='k', ls='--')
                ax.plot(x,x**2*yc, label='', color=cols[i], ls='-')
            else:
                # compute RAA assuming up and down quark fractions
                ax.plot(x,x**2*yc, label='', color=cols[i], ls='--')
                ax.fill_between(x,x**2*(yc-ym), x**2*(yc+yp), label='', edgecolor='none', facecolor=cols[i],alpha=0.5)
    ax.set_ylabel("$z^3 D^h_i(z)$")
    ax.set_xlim([0.0,1.0])
    ax.set_ylim([0.0,0.10])
    ax.set_xlabel("$z$")

    ax.legend(frameon=False, ncols=2, columnspacing=0.5, loc="upper left", labelspacing=0.2, handlelength=2, title='$\\mu_{FF}=100\\,\\text{GeV}$')
    plt.tight_layout()
    plt.savefig("%s.pdf" % tag) 



# make the plots
plot_pp_spectra_5020GeV()
plot_pp_spectra_5360GeV()
plot_OO_spectra_5360GeV()
plot_RAA()
plot_RAA_ALICE()
plot_RAA_CMS()
plot_RAA_ATLAS()
plot_RAA_ONe()

# LO results for appendix
plot_FF()
plot_isospin_RAA()
plt.show()
